import frappe
from frappe.model.document import Document

from pdf_a_3.utils.ghostscript import is_ghostscript_installed, get_ghostscript_version


class PDFASettings(Document):
	pass


@frappe.whitelist()
def check_ghostscript():
	"""Check if Ghostscript is installed and return status info."""
	installed = is_ghostscript_installed()
	version = get_ghostscript_version() if installed else None

	if installed:
		return {
			"status": "ok",
			"message": f"Ghostscript is installed. Version: {version}",
		}
	else:
		return {
			"status": "error",
			"message": "Ghostscript is NOT installed. Please install it to enable PDF/A-3 conversion.",
		}
