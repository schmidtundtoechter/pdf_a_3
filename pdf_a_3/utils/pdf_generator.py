"""PDF generation and PDF/A-3 conversion utilities."""

import frappe
from frappe import _
from frappe.translate import print_language

from pdf_a_3.utils.ghostscript import convert_pdf_to_pdfa, is_ghostscript_installed


def generate_pdfa(doc, print_format=None, letter_head=None) -> bytes:
	"""Generate a PDF/A-3 for the given document.

	Args:
		doc: The Frappe document.
		print_format: Print format name. Falls back to default.
		letter_head: Letter head name. Falls back to default.

	Returns:
		PDF/A-3 bytes.
	"""
	if not is_ghostscript_installed():
		frappe.throw(
			_("Ghostscript is not installed. Cannot generate PDF/A-3. Please check PDFA Settings.")
		)

	print_format = print_format or doc.meta.default_print_format or "Standard"
	fallback_language = frappe.db.get_single_value("System Settings", "language") or "en"
	lang = getattr(doc, "language", fallback_language)

	with print_language(lang):
		pdf_data = _get_pdf_data(doc.doctype, doc.name, print_format, letter_head)

	pdfa_data = convert_pdf_to_pdfa(pdf_data)
	return pdfa_data


def _get_pdf_data(doctype, name, print_format, letter_head) -> bytes:
	"""Generate standard PDF from a document."""
	html = frappe.get_print(doctype, name, print_format, letterhead=letter_head)
	return frappe.utils.pdf.get_pdf(html)


def attach_pdfa(doc, pdfa_data: bytes) -> "frappe.core.doctype.file.file.File":
	"""Attach PDF/A-3 data as a file to the document.

	Args:
		doc: The Frappe document.
		pdfa_data: The PDF/A-3 bytes.

	Returns:
		The created File document.
	"""
	file_name = f"{doc.name}.pdf".replace("/", "-")

	file_doc = frappe.new_doc("File")
	file_doc.file_name = file_name
	file_doc.content = pdfa_data
	file_doc.is_private = 1
	file_doc.attached_to_doctype = doc.doctype
	file_doc.attached_to_name = doc.name
	file_doc.save(ignore_permissions=True)

	return file_doc
