import chromadb
from chromadb.utils import embedding_functions
from transformers import pipeline

# Load embedding function (same as before)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./app/retriever/chroma_db")
collection = chroma_client.get_or_create_collection(name="notes", embedding_function=embedding_func)

# Load Hugging Face model for question answering (flan-t5 works well)
print("Loading Hugging Face model...")
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")
print("Model loaded.")


def ask_question(question: str):
    print(f"\n Question: {question}")

    # Step 1: Retrieve relevant documents
    print("Retrieving relevant notes from ChromaDB...")
    results = collection.query(
        query_texts=[question],
        n_results=10
    )

    retrieved_docs = [doc for doc in results["documents"][0] if len(doc) > 50]
    context = "\n".join(retrieved_docs)  # pick top 5 longer chunks
    print(f"Retrieved Context:\n{context}\n")

    # Step 2: Prepare prompt for the model
    prompt = f"You are a helpful assistant. Answer the question in detail using the context below.\n\nContext:\n{context}\n\nQuestion: {question}"

    # Step 3: Generate answer
    print("Generating answer...")
    answer = qa_pipeline(prompt, max_new_tokens=200)[0]['generated_text']
    print(f"Answer:\n{answer}")
    return answer

'''
# Run this to test
if __name__ == "__main__":
    ask_question("What is RAG and how does it work?")
'''