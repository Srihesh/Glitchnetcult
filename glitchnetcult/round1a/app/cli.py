#!/usr/bin/env python3
"""
Round1A CLI: Extract outlines from PDFs in /app/input (Docker) or ../input (local).
Write JSON to /app/output or ../output.
"""

import pathlib
import sys
import time
from round1a.app.extractor import extract_outline, save_json
from round1a.app.utils import setup_logging

import logging

def main():
    setup_logging("outline-extractor")
    logger = logging.getLogger("outline-extractor")


    # Use project-level input/output directories
    BASE_DIR = pathlib.Path(__file__).resolve().parents[2]
    IN_DIR = BASE_DIR / "input"
    OUT_DIR = BASE_DIR / "output"

    # If running locally, override to relative paths (uncomment if needed)
    # IN_DIR = pathlib.Path("../input")
    # OUT_DIR = pathlib.Path("../output")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pdfs = list(IN_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {IN_DIR}", file=sys.stderr)
        return

    t0 = time.perf_counter()
    for pdf in pdfs:
        print(f"Extracting outline: {pdf.name}")
        try:
            result = extract_outline(str(pdf))
            save_json(result, OUT_DIR / (pdf.stem + ".json"))
        except Exception as e:
            logger.error(f"Failed to process {pdf.name}: {e}")
    print(f"Processed {len(pdfs)} file(s) in {time.perf_counter()-t0:.2f}s")

if __name__ == "__main__":
    main()
