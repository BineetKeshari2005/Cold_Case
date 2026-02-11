from src.loader import load_documents
from src.embedder import create_embeddings
from src.retriever import build_index, search
from src.rag_pipeline import build_context, generate_answer


documents = load_documents()


embeddings = create_embeddings(documents)


index = build_index(embeddings)


question = "What do we know about the suspect’s vehicle and when was it seen?"


retrieved_docs = search(index, documents, question, k=3)

print("\nRetrieved Documents:\n")
for doc in retrieved_docs:
    print(doc)


context = build_context(retrieved_docs)


answer = generate_answer(context, question)

print("\nFINAL ANSWER:\n")
print(answer)
