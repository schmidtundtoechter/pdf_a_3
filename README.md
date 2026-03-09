## Pdf A 3

Written for: ERPNext 15.

Compatible with EU Invoice (The app to generate and import invoices as E-Rechnung and X-Rechnung and saves Sales Invoices as PDF/A-3.)
https://github.com/alyf-de/eu_einvoice


## What It Does:
first of all please check the:
“ PDFA Settings “

On Submit of any configured DocType:
- Checks if the DocType is enabled in PDFA Settings.
- Generates PDF using Frappe's standard print engine.
- Converts to PDF/A-3B using Ghostscript.
- Attaches the PDF/A-3B to the document.
- Emails the PDF to the archive email address (if configured).


## Settings Page (PDFA Settings)

Enabled checkbox (global on/off)
Document Types table: Enable per DocType with print format + letter head
Archive Email Address: Optional - for forwarding PDFs on submit
Ghostscript Status: Shows if Ghostscript is installed + version
Check Ghostscript button: Manual check
Installation Instructions: How to install Ghostscript

The resulting PDFs can be tested here: https://www.pdf2go.com/de/pdfa-validieren


## License

mit
