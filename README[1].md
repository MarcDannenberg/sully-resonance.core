# 🧠 Sully Resonance Core

Sully is a symbolic cognition engine — a recursive, paradox-aware AI built to ingest meaning, generate dreams, and explore emergent intelligence.

## 🚀 Features

- 🔮 Symbolic Reasoning + Paradox Synthesis
- 🌌 Dream Generator (`/api/sully/dream`)
- ♾️ Math + Symbol Translator
- 📖 Book Ingestion with OCR
- 🧬 Fusion Engine + Claim Evaluator
- 🌐 FastAPI Backend, ready for Render

## 📡 API Endpoints

- `POST /api/sully/chat` — Send Sully a symbolic message
- `GET /api/sully/dream?seed=...`
- `POST /api/sully/evaluate` — Claim truth scoring
- `GET /api/sully/translate?phrase=...`
- `POST /api/sully/fuse` — Symbol fusion
- `GET /api/sully/paradox?topic=...`

## 📦 Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## ⚙️ Deployment

Ready to deploy to Render using the included `render.yaml`.

---

Built by [Marc Dannenberg](https://github.com/MarcDannenberg)  
Symbolic cognition begins inward.