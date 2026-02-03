"""Ghostscript utility functions for PDF/A-3 conversion."""

import os
import re
import shutil
import subprocess


def is_ghostscript_installed() -> bool:
	"""Check if Ghostscript is installed on the system."""
	return shutil.which("gs") is not None


def get_ghostscript_version() -> str | None:
	"""Return the Ghostscript version string, or None if not installed."""
	if not is_ghostscript_installed():
		return None

	try:
		result = subprocess.run(
			["gs", "--version"], capture_output=True, text=True, timeout=10
		)
		return result.stdout.strip()
	except Exception:
		return None


def _get_icc_profile_path() -> str:
	"""Get the path to the ICC profile directory used by Ghostscript."""
	gs_output = subprocess.run(
		["gs", "-h"], capture_output=True, text=True, timeout=10
	)

	search_paths = re.search(
		r"Search path:([\s\S]+) (\/.+\/lib) ([\s\S]+)Ghostscript",
		gs_output.stdout,
		re.DOTALL,
	)
	if not search_paths:
		raise RuntimeError("Unable to find /lib path in Ghostscript search paths")

	library_path = search_paths.group(2).strip()
	icc_path = os.path.join(library_path[:-4], "iccprofiles")

	if not os.path.exists(icc_path):
		raise RuntimeError(
			"Unable to find ICC profiles folder in Ghostscript search paths."
		)

	return icc_path


def convert_pdf_to_pdfa(pdf_data: bytes) -> bytes:
	"""Convert PDF data to PDF/A-3 format using Ghostscript.

	Args:
		pdf_data: The raw PDF bytes.

	Returns:
		The converted PDF/A-3 bytes.

	Raises:
		RuntimeError: If Ghostscript conversion fails.
	"""
	cwd = None
	if not os.path.isfile("srgb.icc"):
		cwd = _get_icc_profile_path()

	with subprocess.Popen(
		[
			"gs",
			"-q",
			"-sstdout=%stderr",
			"-dPDFA=3",
			"-dBATCH",
			"-dNOPAUSE",
			"-dPDFACompatibilityPolicy=2",
			"-sColorConversionStrategy=RGB",
			"--permit-file-read=srgb.icc",
			"-sDEVICE=pdfwrite",
			"-sOutputFile=-",
			"PDFA_def.ps",
			"-",
		],
		cwd=cwd,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	) as proc:
		pdfa_data, err = proc.communicate(input=pdf_data)
		if proc.returncode != 0:
			raise RuntimeError(f"Ghostscript error: {err.decode()}")
		return pdfa_data
