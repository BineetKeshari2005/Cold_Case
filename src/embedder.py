from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(documents):
    texts = [doc["content"] for doc in documents]
    embeddings = model.encode(texts)
    return np.array(embeddings).astype("float32")
