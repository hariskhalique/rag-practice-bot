import hashlib

from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
import chromadb
import os

# Initialize embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./app/retriever/chroma_db")

# Create collection with correct embedding function
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = chroma_client.get_or_create_collection(
    name="notes",
    embedding_function=embedding_func
)


def load_notes(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def get_hash_id(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

def embed_and_store(file_path: str):
    raw_text = load_notes(file_path)

    # For now, treat each sentence as a document
    docs = [s.strip() for s in raw_text.split(".") if s.strip()]

    # Generate embeddings
    embeddings = embedding_model.encode(docs).tolist()

    # Store in ChromaDB
    for i, (doc, embed) in enumerate(zip(docs, embeddings)):
        doc_id = get_hash_id(doc)
        print(f"Using HASHED ID: {doc_id} for document: {doc[:60]}...")
        collection.upsert(
            ids=[doc_id],
            documents=[doc],
            embeddings=[embed]
        )
    print(f"Stored {len(docs)} documents in ChromaDB.")

'''
if __name__ == "__main__":
    embed_and_store("app/data/sample_notes.txt")
'''