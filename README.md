# 🧱 LEGO RAG

### Build your RAG the way you built spaceships as a kid — brick by brick.

<p align="center">
  <img src="assets/mascot.png" alt="A developer sitting with a stack of docs, ready to feed the bricks" width="280" />
</p>

> ⚠️ **Work in progress.** This is early boilerplate — expect rough edges and
> breaking changes.

Snap bricks (Source → Chunker → Embedder → Vector Store → Retriever →
Reranker → LLM → Output) together on a canvas, connect your repo, and watch a
RAG pipeline get generated to match.

---

## 📁 Project layout

```
LEGO-rag/
├── frontend/   🧱 the canvas (React + Vite + TS)
└── backend/    🧠 the brain (FastAPI)
```

---

## 🚀 Quickstart

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # add your API keys
uvicorn main:app --reload     # http://localhost:8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev                   # http://localhost:5173
```

---

## 🗺️ Roadmap

- [x] Brick catalog + canvas scaffold
- [x] Repo analyzer stub
- [x] Code generator stub
- [ ] Real stud-validation (only compatible bricks connect)
- [ ] Live cost & memory estimator
- [ ] Domain-aware brick recommendations
- [ ] One-click export to a runnable repo

---

## 🤝 Contributing

Got a brick idea or a better default? Open an issue or a PR.
