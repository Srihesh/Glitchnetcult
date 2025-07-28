"""
Extract title and outline from PDF pages represented as dicts.
"""
import json
import pathlib
import logging
from typing import Dict
from round1a.app.pdf_loader import load_pdf_text
from round1a.app.features import page_features, classify

def extract_outline(pdf_path: str) -> Dict:
    logger = logging.getLogger("extractor")
    pages = load_pdf_text(pdf_path)  # List of page dicts
    outline = []
    title = ""
    for idx, page_dict in enumerate(pages, start=1):
        feats = classify(page_features(page_dict))
        if idx == 1 and feats["H1"]:
            title = feats["H1"][0]["text"]
        for level in ("H1", "H2", "H3"):
            for span in feats[level]:
                outline.append({
                    "level": level,
                    "text": span["text"],
                    "page": idx
                })
    logger.info("Extracted outline from %s: %d sections", pdf_path, len(outline))
    return {"title": title, "outline": outline}

def save_json(result: Dict, out_path: pathlib.Path):
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
