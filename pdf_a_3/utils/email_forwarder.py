"""Email forwarding utility for archiving PDF/A-3 files."""

import frappe
from frappe import _


def forward_pdf_to_archive(doc, file_doc):
	"""Enqueue sending the PDF/A-3 to the archive address (runs after commit)."""
	settings = frappe.get_single("PDFA Settings")
	if not settings.archive_email:
		return

	frappe.enqueue(
		"pdf_a_3.utils.email_forwarder._send_archive_email",
		file_name=file_doc.name,
		doctype=doc.doctype,
		docname=doc.name,
		enqueue_after_commit=True,
	)


def _send_archive_email(file_name, doctype, docname):
	"""Background job: read attached PDF/A-3 from disk and send to archive."""
	settings = frappe.get_single("PDFA Settings")
	archive_email = settings.archive_email
	if not archive_email:
		return

	file_doc = frappe.get_doc("File", file_name)
	file_path = file_doc.get_full_path()

	try:
		with open(file_path, "rb") as f:
			content = f.read()
	except OSError:
		frappe.log_error(
			title=f"PDF/A-3 archive: cannot read file {file_path}",
			message=frappe.get_traceback(),
			reference_doctype=doctype,
			reference_name=docname,
		)
		return

	subject = _("PDF/A-3 Archive: {0} {1}").format(_(doctype), docname)
	message = _("Please find attached the PDF/A-3 document for {0} {1}.").format(
		_(doctype), docname
	)

	frappe.sendmail(
		recipients=[archive_email],
		subject=subject,
		message=message,
		attachments=[{"fname": file_doc.file_name, "fcontent": content}],
		now=True,
	)

	frappe.logger("pdf_a_3").info(
		f"PDF/A-3 for {doctype} {docname} sent to archive: {archive_email}"
	)
