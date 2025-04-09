import chromadb
from chromadb.utils import embedding_functions
import hashlib

#Load the shared embedding function
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Persistent Chroma client (single shared DB path)
chroma_client = chromadb.PersistentClient(path="./app/retriever/chroma_db")

# Reusable function to get or create a collection
def get_collection(collection_name: str):
    return chroma_client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_func
    )


def get_hash_id(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()