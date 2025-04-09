from app.retriever.helper import get_collection
from transformers import pipeline

# Load generation model (text2text generation)
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

# Optional: filter short text chunks
def filter_chunks(chunks, min_length=30):
    return [chunk for chunk in chunks if len(chunk.strip()) >= min_length]

def ask_question_with_context(
        question: str,
        source: str = "Resume",
        style: str = "Default"
) -> str:
    print(f"\nQuestion: {question} (Source: {source})")

    retrieved_chunks = []

    # Query resume collection
    if source in ["Resume", "Both"]:
        resume_collection = get_collection("resumes_collection")
        resume_results = resume_collection.query(
            query_texts=[question],
            n_results=5
        )
        resume_docs = resume_results["documents"][0]
        resume_docs = filter_chunks(resume_docs)
        retrieved_chunks.extend(resume_docs)
        print(f"Retrieved {len(resume_docs)} resume chunks")

    # Query job description collection
    if source in ["Job Description", "Both"]:
        job_collection = get_collection("jobs_collection")
        job_results = job_collection.query(
            query_texts=[question],
            n_results=5
        )
        job_docs = job_results["documents"][0]
        job_docs = filter_chunks(job_docs)
        retrieved_chunks.extend(job_docs)
        print(f"Retrieved {len(job_docs)} job description chunks")

    if not retrieved_chunks:
        return "No relevant information found in the selected source(s)."

    # Join all retrieved chunks into context
    context = "\n".join(retrieved_chunks)

    # Prompt Template
    if style == "Concise":
        prompt = f"""Answer concisely based only on the context below.

    Context:
    {context}

    Question: {question}
    """
    elif style == "Beginner-friendly":
        prompt = f"""Explain in simple terms using the context below.

    Context:
    {context}

    Question: {question}
    """
    elif style == "Compare Resume vs Job":
        prompt = f"""Compare the resume and job description below. Highlight overlaps and gaps.

    Context:
    {context}

    Question: {question}
    """
    else:
        prompt = f"""You are a helpful assistant. Answer the question based on the context below.

    Context:
    {context}

    Question: {question}
    """

    # Generate the answer using HF model
    print("Generating answer...")
    output = qa_pipeline(prompt, max_new_tokens=256)[0]["generated_text"]
    return output