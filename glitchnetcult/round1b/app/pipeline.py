"""
Orchestrates multi-PDF analysis, full text chunking, and rich output.
"""
import pathlib, json, datetime, logging
from typing import Dict, List
from round1b.app.ranker import rank_sections
import sys, os
if os.path.isdir(os.path.join(os.path.dirname(__file__), '../../round1a/app')):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../round1a/app')))
from extractor import extract_outline


def read_full_page_text(pdf_page):
    return pdf_page.get_text("text")

def chunk_text(text: str, max_length: int = 300):
    words = text.split()
    return [' '.join(words[i:i+max_length]) for i in range(0, len(words), max_length)]

def analyse(collection_dir: str, persona: str, job: str, use_keywords: bool = False) -> Dict:
    logger = logging.getLogger("pipeline")
    docs = []
    all_chunks = []
    import fitz
    for pdf in pathlib.Path(collection_dir).glob("*.pdf"):
        outline = extract_outline(str(pdf))
        logger.info("Analysing PDF: %s", pdf.name)
        # Structured outline sections
        for item in outline["outline"]:
            docs.append({
                "document": pdf.name,
                "page": item["page"],
                "section_title": item["text"],
                "text": item["text"]
            })
        # Full text chunking
        with fitz.open(str(pdf)) as doc:
            for idx, page in enumerate(doc, 1):
                page_text = read_full_page_text(page)
                chunks = chunk_text(page_text)
                for ch in chunks:
                    all_chunks.append({
                        "document": pdf.name,
                        "page": idx,
                        "chunk": ch
                    })
    # Rank sections
    ranked = rank_sections(docs, persona, job, use_keywords=use_keywords)
    ranked_chunks = sorted(
        all_chunks,
        key=lambda c: sum(kw in c["chunk"].lower() for kw in ["trend", "growth", "risk"]),
        reverse=True
    )[:5]
    return {
        "metadata": {
            "documents": [p.name for p in pathlib.Path(collection_dir).glob("*.pdf")],
            "persona": persona,
            "job_to_be_done": job,
            "processed_at": datetime.datetime.utcnow().isoformat() + "Z",
        },
        "extracted_sections": ranked,
        "subsection_analysis": ranked_chunks
    }
