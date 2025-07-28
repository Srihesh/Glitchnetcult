"""
Embeddings utilities using MiniLM.
"""
from sentence_transformers import SentenceTransformer, util

_model = None
def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _model

def similarity(a: str, b: str) -> float:
    model = get_model()
    emb_a = model.encode(a, show_progress_bar=False)
    emb_b = model.encode(b, show_progress_bar=False)
    return util.cos_sim(emb_a, emb_b)[0][0].item()
