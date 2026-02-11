ColdCase 

A Retrieval-Augmented Generation (RAG) Based Detective Assistant

ColdCase is an AI-powered investigative assistant that uses Retrieval-Augmented Generation (RAG) to analyze case documents and answer questions intelligently.
It combines Sentence Transformers for semantic search with an LLM (via OpenRouter) to generate contextual, evidence-based responses.

 Features

 Semantic search over case documents

 Context-aware answers using RAG architecture

 Modular project structure

 Secure API key handling with .env

 Lightweight and easy to run locally


 Project Structure

 ColdCase/
│
├── data/              # Case documents / knowledge base
├── src/               # Core logic (embedding, retrieval, generation)
├── main.py            # Entry point
├── .gitignore
└── README.md
