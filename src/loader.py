import os

DATA_PATH = "data"

def load_documents():
    documents = []

    for filename in os.listdir(DATA_PATH):
        filepath = os.path.join(DATA_PATH, filename)

        with open(filepath, "r") as file:
            text = file.read()

        documents.append({
            "content": text,
            "source": filename
        })

    return documents
