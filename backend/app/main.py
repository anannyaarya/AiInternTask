from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import pdfplumber
import os
import shutil
import openai

app = FastAPI()

# CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "backend/data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Placeholder: Normally, you'd initialize vector DB here
vector_db = {}

# Replace with your OpenAI key for real use
openai.api_key = "sk-REPLACE_ME"

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Determine file type and extract text accordingly
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_location)
    elif file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        text = extract_text_from_image(file_location)
    else:
        return JSONResponse(content={"error": "Unsupported file type"}, status_code=400)

    # Here you would add to your vector DB or document storage
    vector_db[file.filename] = text

    return {"filename": file.filename, "message": "File uploaded and processed."}

@app.post("/query/")
async def query_documents(query: str = Form(...)):
    # Simulate a GPT response with theme synthesis
    # Normally you'd use FAISS/LangChain here
    dummy_response = {
        "themes": [
            {
                "theme": "Regulatory Compliance",
                "documents": ["DOC001", "DOC003"],
                "summary": "Documents discuss compliance with regulations such as SEBI and LODR."
            },
            {
                "theme": "Penalty Enforcement",
                "documents": ["DOC002"],
                "summary": "Explanation of penalties under relevant legal frameworks."
            }
        ]
    }

    return dummy_response

@app.get("/")
def read_root():
    return {"message": "Document Theme Identifier Chatbot is running."}
