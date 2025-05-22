# Document Research & Theme Identification Chatbot

## Overview

This project implements an interactive chatbot designed for research across large sets of documents (75+), capable of identifying common themes and providing detailed, cited responses to user queries. It supports uploading PDFs and scanned images, performs OCR on scanned documents, and uses vector databases for semantic search and theme extraction.

---

## Features

- Upload multiple documents (PDFs, scanned images)
- OCR preprocessing for scanned documents (using Tesseract)
- Store and manage documents in a backend database
- Query documents in natural language
- Extract relevant text with precise citations (page and paragraph)
- Identify and synthesize common themes across documents
- Provide final answers with clear theme-based citations
- Simple frontend interface to upload files and ask questions

---

## Technologies Used

- **Backend**: Python, FastAPI, Tesseract OCR, vector search (Qdrant)
- **Frontend**: Basic HTML, JavaScript (Fetch API)
- **Database**: Vector database (Qdrant)
- **AI Models**: OpenAI GPT (or compatible LLM) for query understanding and theme synthesis
- **Deployment**: Compatible with platforms like Render, Railway, Vercel, etc.

---

## Setup Instructions

### Backend

1. Create and activate a Python virtual environment:

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows PowerShell
2. Install dependencies:

pip install -r requirements.txt

3. Start the backend server:
uvicorn app.main:app --reload
The backend will be available at http://localhost:8000

Frontend
Open frontend/index.html in a browser.

Use the interface to upload documents and submit queries.

The frontend communicates with the backend API at http://localhost:8000.

How to Use
Upload multiple documents via the Upload Document section.

After processing, enter your query in the Ask a Question section.

Receive individual document answers with citations and synthesized themes.

View results in JSON format with clear references to document IDs and text locations.

Project Structure
chatbot_theme_identifier/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── services/
│   │   ├── main.py
│   │   └── config.py
│   ├── data/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   └── index.html
├── docs/
├── tests/
├── demo/
└── README.md
Challenges and Future Work
Improving citation granularity (sentence-level citations)

Adding a document filtering UI based on metadata (author, date, relevance)

Enhancing UI/UX for better user experience

Supporting more document formats and batch uploads

Integration with advanced LLMs like Gemini or Groq

Thank you for reviewing my submission!


