import numpy as np
from sentence_transformers import SentenceTransformer

def load_model(model_name="all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)

def embed_text(model, chunks):
    return np.array(model.encode(chunks))
