"""
Feature extraction: identify headings with font size, ALL CAPS, underline heuristics.
"""
from typing import Dict

BIG_FONT_THRESHOLD = 1.15

def is_all_caps(text: str) -> bool:
    return text.isupper() and len(text) > 2

def is_underlined(span: dict) -> bool:
    return span.get('flags', 0) & 4

def page_features(page_dict: dict) -> list:
    """
    Extract features from PDF page dict (not page object).
    Returns list of span dicts with feature flags.
    """
    spans = []
    for block in page_dict.get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                s = {
                    "text": span["text"].strip(),
                    "size": span["size"],
                    "font": span.get("font", ""),
                    "flags": span.get("flags", 0),
                    "y0": span["bbox"][1],
                    "y1": span["bbox"][3],
                    "is_all_caps": is_all_caps(span["text"]),
                    "underline": is_underlined(span),
                }
                spans.append(s)
    return spans

def classify(spans: list) -> Dict[str, list]:
    """
    Assign each span to H1/H2/H3/body with improved heuristics.
    """
    sizes = [s["size"] for s in spans if s["text"]]
    med = sorted(sizes)[len(sizes)//2] if sizes else 0
    buckets = {"H1": [], "H2": [], "H3": [], "body": []}
    for s in spans:
        if not s["text"]:
            continue
        rel = s["size"] / (med or 1)
        if s["is_all_caps"]:
            buckets["H2"].append(s)
        elif s["underline"]:
            buckets["H3"].append(s)
        elif rel > BIG_FONT_THRESHOLD * 1.5:
            buckets["H1"].append(s)
        elif rel > BIG_FONT_THRESHOLD * 1.2:
            buckets["H2"].append(s)
        elif rel > BIG_FONT_THRESHOLD:
            buckets["H3"].append(s)
        else:
            buckets["body"].append(s)
    return buckets
