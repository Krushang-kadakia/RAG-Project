from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

client = QdrantClient("http://localhost", port=6333)
collection_name = "rag_chunks"

def store_embeddings(embeddings, chunks):
    # Only create the collection if it doesn't exist
    try:
        client.get_collection(collection_name=collection_name)
    except Exception:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=len(embeddings[0]), distance=Distance.COSINE),
        )

    # Generate unique integer IDs by counting existing records
    current_count = client.count(collection_name=collection_name).count

    points = [
        PointStruct(
            id=current_count + i,
            vector=vector,
            payload={"text": chunk}
        )
        for i, (chunk, vector) in enumerate(zip(chunks, embeddings))
    ]

    client.upsert(collection_name=collection_name, points=points)

def retrieve_relevant_chunks(question, model, top_k=5, threshold=0.5):
    query_embedding = model.encode(question).tolist()

    search_results = client.search(
        collection_name=collection_name,
        query_vector=query_embedding,
        limit=top_k,
        with_vectors=False,
        with_payload=True
    )

    filtered = [
        hit.payload["text"] for hit in search_results if hit.score >= threshold
    ]

    if not filtered:
        filtered = [search_results[0].payload["text"]] if search_results else []

    return filtered

def retrieve_all_chunks_from_storage():
    points = client.scroll(
        collection_name=collection_name,
        limit=10000,
        with_payload=True
    )
    chunks = [point.payload["text"] for point in points[0]]
    return chunks
