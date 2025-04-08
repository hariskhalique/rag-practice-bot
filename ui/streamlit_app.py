import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from app.retriever.embed_and_store import embed_and_store
from app.retriever.query_and_generate import ask_question
import os

st.set_page_config(page_title="RAG Chatbot", page_icon="")

st.title("Retrieval-Augmented Generation (RAG) Chatbot")

st.sidebar.header("Upload Notes")

# Upload notes
uploaded_file = st.sidebar.file_uploader("Upload your notes (.txt only)", type=["txt"])
if uploaded_file is not None:
    file_path = os.path.join("app/data", uploaded_file.name)
    with open(file_path, "w") as f:
        f.write(uploaded_file.getvalue().decode("utf-8"))
    st.sidebar.success("Notes uploaded.")

    # Only allow embedding once per session unless user clears it
    if "embedded" not in st.session_state:
        st.session_state.embedded = False

    if st.sidebar.button("Embed Notes") and not st.session_state.embedded:
        embed_and_store(file_path)
        st.session_state.embedded = True
        st.sidebar.success("Notes embedded and stored!")
    elif st.session_state.embedded:
        st.sidebar.info("Notes already embedded in this session.")

st.markdown("---")

# Question box
question = st.text_input("Ask a question based on your notes:")

# Get Answer
if question:
    with st.spinner("Thinking....."):
        answer = ask_question(question)
        st.success("Answer:")
        st.write(answer)