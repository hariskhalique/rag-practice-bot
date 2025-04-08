# RAG Chatbot — Retrieval-Augmented Generation Assistant

A beginner-friendly, open-source RAG chatbot built using:
- ChromaDB for vector search
- SentenceTransformers for embeddings
- Hugging Face models for generation
- Streamlit for the frontend UI

---

## Features

- Upload your notes or `.txt` documents
- Embed them using Sentence Transformers
- Ask questions in natural language
- Retrieve relevant chunks using vector similarity
- Generate answers using Hugging Face models
- Streamlit-based interface for ease of use

---

## Project Structure

```
rag-chatbot/
├── app/
│   ├── data/                  # Uploaded notes
│   ├── retriever/
│   │   ├── embed_and_store.py     # Embeds and stores notes
│   │   └── query_and_generate.py  # Retrieves context and answers
│   └── generator/             # (Optional: future use)
├── ui/
│   └── streamlit_app.py       # Streamlit frontend
├── requirements.txt
└── README.md
```

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/yourname/rag-chatbot.git
cd rag-chatbot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run ui/streamlit_app.py
```

---

## How It Works

1. Upload notes as text files
2. Split into sentences → Embed using `all-MiniLM-L6-v2`
3. Store in ChromaDB
4. Ask a question → Convert to embedding → Find top matches
5. Construct a prompt → Generate an answer using `flan-t5-base`

---

## Models Used

- **Embeddings**: `all-MiniLM-L6-v2`
- **Generator**: `google/flan-t5-base`

You can replace these with any SentenceTransformer or Hugging Face model.

---

## To Do / Extend

- [ ] Add PDF and DOCX support
- [ ] Add memory/chat history
- [ ] Add source highlighting for retrieved chunks
- [ ] Dockerize the app

---

## License

MIT License. Feel free to use and contribute!

