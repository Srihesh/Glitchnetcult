"""
Routines for importance ranking: MiniLM vs custom keyword-based scoring.
"""
from typing import List, Dict
from round1b.app.embedding import similarity

KEYWORDS = ["financial", "trend", "growth", "investment", "risk"]

def keyword_score(text: str, query: str) -> float:
    # Simple keyword intersection
    score = sum(1 for kw in KEYWORDS if kw.lower() in text.lower())
    return score / len(KEYWORDS)  # normalize

def rank_sections(sections: List[Dict], persona: str, job: str, use_keywords: bool = False) -> List[Dict]:
    """
    Flexible ranker: MiniLM similarity or keyword match.
    """
    query = f"{persona}. Task: {job}"
    for s in sections:
        if use_keywords:
            s["score"] = keyword_score(s["text"], query)
        else:
            s["score"] = similarity(query, s["text"])
    return sorted(sections, key=lambda x: x["score"], reverse=True)
