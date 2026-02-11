import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def build_context(retrieved_docs):
    context = ""
    for doc in retrieved_docs:
        context += f"Source: {doc['source']}\n"
        context += f"Content: {doc['content']}\n\n"
    return context

def generate_answer(context, question):

    prompt = f"""
You are a detective assistant.

Answer ONLY using the evidence below.
You MUST cite the source filename in brackets.

Evidence:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
