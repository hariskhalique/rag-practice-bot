import os
from app.retriever.helper import get_hash_id, get_collection

# Get or create a separate collection for job descriptions
collection = get_collection("jobs_collection")


# Main function to embed and store job description chunks
def embed_job(file_path: str):
    print(f"Reading job description from: {file_path}")

    with open(file_path, "r") as f:
        content = f.read()

    # Split into short chunks (per line or sentence)
    chunks = [line.strip() for line in content.split("\n") if len(line.strip()) > 30]

    print(f"Found {len(chunks)} meaningful chunks in job description")

    for chunk in chunks:
        doc_id = get_hash_id(chunk)
        collection.upsert(
            ids=[doc_id],
            documents=[chunk],
            metadatas=[{"type": "job", "source_file": os.path.basename(file_path)}]
        )
        print(f"Upserted job chunk: {chunk[:60]}...")

    print("Job description embedded successfully")