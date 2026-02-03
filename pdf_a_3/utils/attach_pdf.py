"""Main on_submit handler for PDF/A-3 generation and archiving."""

import frappe
from frappe import _

from pdf_a_3.utils.ghostscript import is_ghostscript_installed
from pdf_a_3.utils.pdf_generator import generate_pdfa, attach_pdfa
from pdf_a_3.utils.email_forwarder import forward_pdf_to_archive


def on_submit(doc, event=None):
	"""Hook called when a document is submitted.

	Checks PDFA Settings to see if this DocType is enabled,
	then generates PDF/A-3, attaches it, and optionally emails to archive.
	"""
	settings = frappe.get_single("PDFA Settings")

	if not settings.enabled:
		return

	enabled_row = _get_enabled_row(settings, doc.doctype)
	if not enabled_row:
		return

	if not is_ghostscript_installed():
		frappe.log_error(
			title=_("Ghostscript not installed"),
			message=_("Cannot generate PDF/A-3 for {0} {1}. Ghostscript is not installed.").format(
				doc.doctype, doc.name
			),
			reference_doctype=doc.doctype,
			reference_name=doc.name,
		)
		return

	frappe.enqueue(
		method=_process_pdfa,
		queue="default",
		timeout=60,
		now=bool(frappe.flags.in_test or frappe.conf.developer_mode),
		enqueue_after_commit=True,
		doctype=doc.doctype,
		docname=doc.name,
		print_format=enabled_row.print_format,
		letter_head=enabled_row.letter_head,
	)


def _process_pdfa(doctype, docname, print_format=None, letter_head=None):
	"""Background job: generate PDF/A-3, attach, and email to archive.

	Args:
		doctype: The document type.
		docname: The document name.
		print_format: Print format to use.
		letter_head: Letter head to use.
	"""
	try:
		doc = frappe.get_doc(doctype, docname)
		pdfa_data = generate_pdfa(doc, print_format=print_format, letter_head=letter_head)
		file_doc = attach_pdfa(doc, pdfa_data)
		forward_pdf_to_archive(doc, file_doc)

		frappe.logger("pdf_a_3").info(
			f"PDF/A-3 generated and attached for {doctype} {docname}"
		)
	except Exception:
		frappe.log_error(
			title=_("PDF/A-3 Generation Failed"),
			message=frappe.get_traceback(),
			reference_doctype=doctype,
			reference_name=docname,
		)


def _get_enabled_row(settings, doctype):
	"""Return the matching enabled row for the given DocType, or None."""
	for row in settings.enabled_for:
		if row.document_type == doctype and row.enabled:
			return row
	return None
