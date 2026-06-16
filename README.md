# 🧱 LEGO RAG

### Build your RAG the way you built spaceships as a kid — brick by brick.

<p align="center">
  <img src="assets/mascot.png" alt="A developer sitting with a stack of docs, ready to feed the bricks" width="280" />
</p>

<p align="center"><i>Every RAG starts with a pile of knowledge — we help you snap it into shape. 🧱📚</i></p>

> Snap blocks together on a canvas. Connect your repo. Watch a production-ready
> RAG pipeline assemble itself in the background, perfectly aligned to the
> bricks you clicked together.

```
        ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
        │  📥 LOAD  │────▶│ ✂️ CHUNK │────▶│ 🧬 EMBED │────▶│ 🗄️ STORE │
        └──────────┘     └──────────┘     └──────────┘     └──────────┘
                                                                  │
        ┌──────────┐     ┌──────────┐     ┌──────────┐           │
        │ 📤 ANSWER │◀────│  🧠 LLM  │◀────│ 🔎 RETRY │◀──────────┘
        └──────────┘     └──────────┘     └──────────┘
                       snap. connect. ship. 🚀
```

---

## ✨ Why LEGO RAG?

Building a Retrieval-Augmented Generation system today means a thousand tiny
decisions — *which chunker? which embedder? which vector store? how big is the
context window? what does this cost at scale?* — and most of them are made
blindly, then regretted in production.

**LEGO RAG turns those decisions into bricks.**

You drag bricks onto a canvas, click them together, and connect your repository.
Because you connected the *actual* repo, we analyze the *actual* code, docs, and
data so every brick is recommended for **your** domain — not a generic tutorial.
Behind the scenes, the wiring you snap together is compiled into real,
runnable RAG code.

It's a builder's toy with a production engine underneath.

---

## 🧩 The Bricks

Every RAG is the same eight kinds of brick, snapped in a different order.

| Brick | What it does | Example studs |
|-------|--------------|---------------|
| 📥 **Source** | Pulls in your knowledge | Repo connector, PDFs, web, Notion |
| ✂️ **Chunker** | Splits docs into bite-size pieces | Recursive, semantic, token, markdown |
| 🧬 **Embedder** | Turns text into vectors | OpenAI, Cohere, local / HF models |
| 🗄️ **Vector Store** | Remembers everything | Chroma, FAISS, pgvector, Pinecone |
| 🔎 **Retriever** | Finds the relevant pieces | Similarity, MMR, hybrid (BM25 + vector) |
| 🎚️ **Reranker** | Sorts the good from the great | Cross-encoder, Cohere rerank |
| 🧠 **LLM** | Reasons over the context | Claude, GPT, local models |
| 📤 **Output** | Shapes the final answer | Cited answer, JSON, streaming chat |

Snap them in any valid order and the canvas validates the connection — square
studs only fit square holes. 🔌

---

## 🎯 Bricks tuned to your constraints

Tell LEGO RAG what you care about and it recolors the brick palette to match.
The same pipeline looks different depending on what you optimize for:

- ⚙️ **Production-readiness** — battle-tested bricks, retries, observability
- 📈 **Scalability** — bricks that survive millions of documents
- 🧭 **Domain** — legal? medical? code? bricks pick domain-aware defaults
- 💸 **Cost** — see the $ per 1k queries before you ship
- 🧠 **Memory** — fit your index in the RAM you actually have
- 🎟️ **Context tokens** — never blow your model's context window again

The analyzer reads these alongside your connected repo and suggests the brick
set that fits — then *you* make the final click.

---

## 🛠️ How it works

```
   ┌────────────────────┐        ┌─────────────────────┐
   │   🧱 The Canvas     │        │     🧠 The Brain     │
   │   (frontend)        │        │     (backend)        │
   │                     │  graph │                     │
   │  drag • snap • wire ├───────▶│  1. analyze repo     │
   │                     │        │  2. validate bricks  │
   │  see live $ / RAM   │◀───────┤  3. generate code    │
   └────────────────────┘  report └─────────────────────┘
```

1. **You build** — drag bricks onto the canvas and connect them.
2. **You connect your repo** — so the analysis reflects your real data.
3. **The brain analyzes** — repo + bricks + your constraints.
4. **Code assembles** — a runnable RAG pipeline, aligned to your bricks.

---

## 📁 Project layout

```
LEGO-rag/
├── README.md
├── frontend/            🧱 the LEGO canvas (React + Vite + TS)
│   ├── src/
│   │   ├── App.tsx
│   │   ├── blocks/catalog.ts      ← the brick definitions
│   │   └── components/            ← palette + canvas
│   └── package.json
└── backend/             🧠 the brain (FastAPI)
    ├── main.py
    └── app/
        ├── blocks/registry.py     ← the brick definitions (mirror)
        ├── analyzer/              ← reads your repo
        ├── generator/            ← turns bricks into code
        └── models/schema.py      ← the wire format
```

> 💡 The brick catalog lives in **both** the frontend (`catalog.ts`) and the
> backend (`registry.py`). Keep them in sync — they speak the same language.

---

## 🚀 Quickstart

### 🧠 Backend (the brain)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # add your API keys
uvicorn main:app --reload     # http://localhost:8000
```

### 🧱 Frontend (the canvas)

```bash
cd frontend
npm install
npm run dev                   # http://localhost:5173
```

Open the canvas, drag your first brick, and start snapping. 🧱

---

## 🗺️ Roadmap

- [x] 🧱 Brick catalog + canvas scaffold
- [x] 🧠 Repo analyzer stub
- [x] 🏗️ Code generator stub
- [ ] 🔌 Real stud-validation (only compatible bricks connect)
- [ ] 💸 Live cost & memory estimator on the canvas
- [ ] 🧭 Domain-aware brick recommendations
- [ ] 📦 One-click export to a runnable repo
- [ ] 🤝 Share & remix other people's builds

---

## 🤝 Contributing

This is early — boilerplate today, brilliant tomorrow. Got a brick idea? A
better default? Open an issue or a PR. Build something cool and show us. 🧱

---

<p align="center"><i>Made with too many bricks and not enough sleep.</i> 🧱💤</p>
