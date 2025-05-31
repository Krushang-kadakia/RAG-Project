import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
from utils.qdrant_handler import retrieve_all_chunks_from_storage

def is_query_relevant(query, model,chunks, threshold=0.2):
    chunks = retrieve_all_chunks_from_storage()

    if not chunks:
        return False

    query_embedding = model.encode([query])
    chunk_embeddings = model.encode(chunks[:20])  # Optional: limit for performance
    sims = cosine_similarity(query_embedding, chunk_embeddings)[0]
    avg_sim = np.mean(sims)

    # print(f"Query: {query}")  # Debugging
    # print(f"Chunk embeddings (first 3 chunks): {chunk_embeddings[:3]}")  # Debugging
    # print(f"Cosine similarities: {sims}")  # Debugging
    # print(f"Avg similarity: {avg_sim}")  # Debugging

    return avg_sim >= threshold
