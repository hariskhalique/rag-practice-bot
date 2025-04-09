import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from app.retriever.embed_resume import embed_resume
from app.retriever.embed_job import embed_job
from app.retriever.query_resume_job import ask_question_with_context

st.set_page_config(page_title="Chat with Your Resume", page_icon="")

st.title("Chat with Your Resume")
st.markdown("Upload your resume and job descriptions, then ask questions about your fit, skills, or summary.")

st.sidebar.header("Upload Files")

# Upload resume
resume_file = st.sidebar.file_uploader("Upload your Resume (.txt)", type=["txt"], key="resume")
if resume_file:
    resume_path = os.path.join("app/data/resumes", resume_file.name)
    with open(resume_path, "w") as f:
        f.write(resume_file.getvalue().decode("utf-8"))
    st.sidebar.success("Resume uploaded")

    if st.sidebar.button("Embed Resume"):
        embed_resume(resume_path)
        st.sidebar.success("Resume embedded")

# Upload job description
job_file = st.sidebar.file_uploader("Upload Job Description (.txt)", type=["txt"], key="job")
if job_file:
    job_path = os.path.join("app/data/jobs", job_file.name)
    with open(job_path, "w") as f:
        f.write(job_file.getvalue().decode("utf-8"))
    st.sidebar.success("Job description uploaded")

    if st.sidebar.button("Embed Job Description"):
        embed_job(job_path)
        st.sidebar.success("Job description embedded")

st.markdown("---")

# Select data source
data_source = st.radio("Chat with:", ["Resume", "Job Description", "Both"])

# Select Prompt Style
prompt_style = st.selectbox(
    "Answer Style",
    ["Default", "Concise", "Beginner-friendly", "Compare Resume vs Job"]
)

# Ask a question
question = st.text_input("Ask a question based on your resume or the job description:")

if question:
    with st.spinner("Thinking....."):
        answer = ask_question_with_context(question, source=data_source, style=prompt_style)
        st.success("Answer:")
        st.write(answer)