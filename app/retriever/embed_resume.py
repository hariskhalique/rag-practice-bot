import os

from app.retriever.helper import get_hash_id, get_collection

# Get or create a separate collection for resumes
collection = get_collection("resumes_collection")


# Main function to embed and store resume chunks
def embed_resume(file_path: str):
    print(f"Reading resume from: {file_path}")

    with open(file_path, "r") as f:
        content = f.read()

    # Split into short chunks (naive split by sentence or line)
    chunks = [line.strip() for line in content.split("\n") if len(line.strip()) > 30]

    print(f"Found {len(chunks)} meaningful chunks in resume")

    for chunk in chunks:
        doc_id = get_hash_id(chunk)
        collection.upsert(
            ids=[doc_id],
            documents=[chunk],
            metadatas=[{"type": "resume", "source_file": os.path.basename(file_path)}]
        )
        print(f"Upserted chunk: {chunk[:60]}...")

    print("Resume embedded successfully")