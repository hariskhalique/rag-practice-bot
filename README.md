# Chat with Your Resume — A RAG-Powered Career Assistant

This project is a Retrieval-Augmented Generation (RAG) application that allows users to:
- Upload their **resume (CV)**
- Upload **job descriptions**
- Ask questions to compare, summarize, or assess their profile against job roles

---

## What Can You Do With This?

- “Summarize my resume.”
- “What skills am I missing based on this job?”
- “Does my resume match this job description?”
- “What technologies should I learn to apply for this role?”

---

## Technologies Used

| Component | Tech |
|----------|------|
| UI | Streamlit |
| Embedding | SentenceTransformers (`all-MiniLM-L6-v2`) |
| Vector DB | ChromaDB |
| Language Model | Hugging Face `flan-t5-base` |
| Prompt Templating | Built-in styles via dropdown |
| Document Types | `.txt` extracted from `.pdf` or job specs |

---

## Project Structure

```
rag-chatbot/
├── app/
│   ├── data/
│   │   ├── resumes/                 # Resume .txt files
│   │   ├── jobs/                    # Job description .txt files
│   ├── retriever/
│   │   ├── embed_resume.py          # Embeds resumes
│   │   ├── embed_job.py             # Embeds job descriptions
│   │   ├── query_resume_job.py      # RAG logic for resume/job Q&A
│   │   └── helper.py                # Shared embedding/model logic
│   ├── templates/
│   │   └── prompt_template.txt      # Prompt formats (optional)
├── ui/
│   └── streamlit_app.py             # Streamlit frontend
├── requirements.txt
├── README.md
```

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/yourname/chat-with-your-resume.git
cd chat-with-your-resume

# 2. Create Virtual Environment 
python -m venv venv ( it will create VE )
source venv/bin/activate ( it activate you VE )

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run ui/streamlit_job_app.py
```

---

## Upload Format

- Supported file: `.txt` (You can extract from PDF using built-in tools)
- Resume is saved in `app/data/resumes/`
- Job descriptions saved in `app/data/jobs/`

---

## Prompt Styles Supported

- **Default** — Basic helpful assistant style
- **Concise** — Short, to-the-point responses
- **Beginner-friendly** — Simplified answers
- **Compare Resume vs Job** — Compares both and highlights matches/mismatches

---

## To Do / Improve

- [ ] PDF/DOCX support with automatic text extraction
- [ ] Add chat history / memory per session
- [ ] Show matched chunks (retrieved documents)
- [ ] Option to export a summarized CV

---

## License

MIT License. Feel free to fork, build, and extend!
