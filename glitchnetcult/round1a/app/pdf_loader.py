"""
PDF Loader utilities: loads PDF pages as dicts (to avoid PyMuPDF page invalidation).
"""
from typing import List
import fitz
import logging

def load_pdf_text(path: str) -> List[dict]:
    """
    Open a PDF and return list of page text dicts.
    Keeps document open only within this function.
    """
    logger = logging.getLogger("pdf_loader")
    try:
        with fitz.open(path) as doc:
            pages = [page.get_text("dict") for page in doc]
            logger.info("Loaded %d pages from %s", len(pages), path)
            return pages
    except Exception as e:
        logger.error("Failed to load PDF [%s]: %s", path, e)
        raise
