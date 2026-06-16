"""🧱 The brick catalog (backend mirror).

Every RAG is the same eight kinds of brick snapped in a different order. This
is the source of truth on the brain side — keep it in sync with the frontend's
`src/blocks/catalog.ts`.

Each brick declares the studs it exposes:
  - `accepts`: which categories can plug INTO it (upstream)
  - `emits`:   which categories it can plug INTO (downstream)
so the canvas can validate that square studs only fit square holes. 🔌
"""

# Ordered stages of a classic RAG pipeline.
CATEGORIES = [
    "source",      # 📥 where knowledge comes from
    "chunker",     # ✂️ split docs into pieces
    "embedder",    # 🧬 text -> vectors
    "vectorstore", # 🗄️ remember the vectors
    "retriever",   # 🔎 find relevant pieces
    "reranker",    # 🎚️ sort good from great (optional)
    "llm",         # 🧠 reason over context
    "output",      # 📤 shape the final answer
]


# brick_type -> definition
REGISTRY: dict[str, dict] = {
    # 📥 sources
    "repo_connector": {
        "category": "source",
        "emoji": "📥",
        "name": "Repo Connector",
        "description": "Pull docs & code straight from your connected repository.",
        "defaults": {"include_globs": ["**/*.md", "**/*.py"], "branch": "main"},
    },
    "pdf_loader": {
        "category": "source",
        "emoji": "📄",
        "name": "PDF Loader",
        "description": "Load a folder of PDFs.",
        "defaults": {"path": "./data"},
    },
    # ✂️ chunkers
    "recursive_splitter": {
        "category": "chunker",
        "emoji": "✂️",
        "name": "Recursive Splitter",
        "description": "Split on paragraphs, then sentences, then words.",
        "defaults": {"chunk_size": 1000, "chunk_overlap": 150},
    },
    "semantic_splitter": {
        "category": "chunker",
        "emoji": "🧩",
        "name": "Semantic Splitter",
        "description": "Split where the meaning shifts. Pricier, sharper chunks.",
        "defaults": {"threshold": 0.75},
    },
    # 🧬 embedders
    "openai_embedder": {
        "category": "embedder",
        "emoji": "🧬",
        "name": "OpenAI Embeddings",
        "description": "text-embedding-3-small / -large.",
        "defaults": {"model": "text-embedding-3-small"},
    },
    "local_embedder": {
        "category": "embedder",
        "emoji": "🏠",
        "name": "Local Embeddings",
        "description": "Run a HuggingFace model on your own hardware. Free, private.",
        "defaults": {"model": "BAAI/bge-small-en-v1.5"},
    },
    # 🗄️ vector stores
    "chroma_store": {
        "category": "vectorstore",
        "emoji": "🗄️",
        "name": "Chroma",
        "description": "Zero-setup local vector store. Great for prototypes.",
        "defaults": {"persist_dir": "./data/vectorstore"},
    },
    "pgvector_store": {
        "category": "vectorstore",
        "emoji": "🐘",
        "name": "pgvector",
        "description": "Vectors in Postgres. Scales with infra you already trust.",
        "defaults": {"table": "embeddings"},
    },
    # 🔎 retrievers
    "similarity_retriever": {
        "category": "retriever",
        "emoji": "🔎",
        "name": "Similarity Retriever",
        "description": "Top-k nearest vectors. The honest default.",
        "defaults": {"k": 4},
    },
    "hybrid_retriever": {
        "category": "retriever",
        "emoji": "🪢",
        "name": "Hybrid Retriever",
        "description": "Blend keyword (BM25) + vector search.",
        "defaults": {"k": 6, "alpha": 0.5},
    },
    # 🎚️ rerankers (optional)
    "cross_encoder_reranker": {
        "category": "reranker",
        "emoji": "🎚️",
        "name": "Cross-Encoder Reranker",
        "description": "Re-score candidates with a heavier model for precision.",
        "defaults": {"top_n": 3},
    },
    # 🧠 llms
    "claude_llm": {
        "category": "llm",
        "emoji": "🧠",
        "name": "Claude",
        "description": "Anthropic's Claude. Big context, strong reasoning.",
        "defaults": {"model": "claude-sonnet-4-6", "max_tokens": 1024},
    },
    "openai_llm": {
        "category": "llm",
        "emoji": "🤖",
        "name": "GPT",
        "description": "OpenAI chat models.",
        "defaults": {"model": "gpt-4o-mini", "max_tokens": 1024},
    },
    # 📤 outputs
    "cited_answer": {
        "category": "output",
        "emoji": "📤",
        "name": "Cited Answer",
        "description": "An answer with inline source citations.",
        "defaults": {"format": "markdown"},
    },
}


def bricks_by_category(category: str) -> list[str]:
    """Return all brick types belonging to a category."""
    return [b for b, spec in REGISTRY.items() if spec["category"] == category]


def get_brick(brick_type: str) -> dict | None:
    """Look up a brick definition, or None if it's not in the catalog."""
    return REGISTRY.get(brick_type)
