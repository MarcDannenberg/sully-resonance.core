import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI, UploadFile, File, Query
from pydantic import BaseModel
import os

# --- Sully Core ---
from sully import Sully

# --- FastAPI App ---
app = FastAPI()
sully = Sully()

# --- Pydantic Models ---
class ChatPrompt(BaseModel):
    message: str
    tone: str = "emergent"

class NewWord(BaseModel):
    term: str
    meaning: str

# --- Identity ---
@app.get("/api/sully/identity")
async def get_identity():
    return sully.identity.to_json()

# --- Chat ---
@app.post("/api/sully/chat")
async def chat_with_sully(prompt: ChatPrompt):
    result = sully.reason(prompt.message, prompt.tone)
    return result

# --- Dictionary ---
@app.get("/api/sully/words")
async def word_count():
    return {"known_words": sully.word_count()}

@app.post("/api/sully/define")
async def define_word(new_word: NewWord):
    sully.define_word(new_word.term, new_word.meaning)
    return {"status": "added", "term": new_word.term}

# --- Dream ---
@app.get("/api/sully/dream")
async def dream(seed: str = Query(...)):
    return sully.dream(seed)

# --- Claim Evaluation ---
@app.post("/api/sully/evaluate")
async def evaluate_claim(prompt: ChatPrompt):
    result = sully.evaluate_claim(prompt.message)
    return result

# --- Math Translation ---
@app.get("/api/sully/translate")
async def translate_math(phrase: str = Query(...)):
    return {
        "original": phrase,
        "translation": sully.translate_math(phrase)
    }

# --- Fusion ---
@app.post("/api/sully/fuse")
async def fuse_symbols(inputs: list[str]):
    return {
        "fusion_result": sully.fuse(*inputs)
    }

# --- Paradox Reveal ---
@app.get("/api/sully/paradox")
async def reveal_paradox(topic: str = Query(...)):
    return {
        "topic": topic,
        "paradox": sully.reveal_paradox(topic)
    }

# --- Book Ingestion via Upload ---
@app.post("/api/sully/ingest")
async def ingest_book(file: UploadFile = File(...)):
    contents = await file.read()
    upload_dir = "temp_uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as f:
        f.write(contents)

    result = sully.ingest_and_store_text(file_path)
    return {
        "status": result,
        "length": len(contents)
    }