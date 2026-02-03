"""Email forwarding utility for archiving PDF/A-3 files."""

import frappe
from frappe import _


def forward_pdf_to_archive(doc, file_doc):
	"""Send the PDF/A-3 attachment to the archive email address.

	Args:
		doc: The Frappe document (Sales Invoice, Quotation, etc.).
		file_doc: The File document containing the PDF/A-3.
	"""
	settings = frappe.get_single("PDFA Settings")
	archive_email = settings.archive_email

	if not archive_email:
		return

	subject = _("PDF/A-3 Archive: {0} {1}").format(_(doc.doctype), doc.name)
	message = _("Please find attached the PDF/A-3 document for {0} {1}.").format(
		_(doc.doctype), doc.name
	)

	file_url = file_doc.file_url
	file_path = file_doc.get_full_path()

	frappe.sendmail(
		recipients=[archive_email],
		subject=subject,
		message=message,
		attachments=[
			{
				"fname": file_doc.file_name,
				"fcontent": open(file_path, "rb").read(),
			}
		],
		now=False,
	)

	frappe.logger("pdf_a_3").info(
		f"PDF/A-3 for {doc.doctype} {doc.name} sent to archive: {archive_email}"
	)
