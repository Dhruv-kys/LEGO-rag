"""🧠 LEGO RAG — the brain.

FastAPI entrypoint. The canvas (frontend) talks to this service to:
  1. analyze a connected repo,
  2. validate the bricks the user snapped together,
  3. generate runnable RAG code aligned to those bricks.

This is boilerplate — every route returns a friendly stub for now.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

app = FastAPI(
    title="🧱 LEGO RAG",
    description="Build your RAG, brick by brick.",
    version="0.1.0",
)

# The canvas runs on a different port during dev — let it talk to the brain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    """Health check / friendly hello."""
    return {"name": "LEGO RAG", "status": "🧱 ready to build", "version": "0.1.0"}
