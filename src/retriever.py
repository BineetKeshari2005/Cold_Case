import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search(index, documents, query, k=2):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = []
    for idx in indices[0]:
        results.append(documents[idx])

    return results
