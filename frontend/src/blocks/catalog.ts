// 🧱 The brick catalog (frontend mirror).
//
// Mirrors the backend's `app/blocks/registry.py`. The canvas can fetch the live
// catalog from `GET /api/bricks`, but this local copy keeps the palette working
// before the brain is even running.

export type Category =
  | "source"
  | "chunker"
  | "embedder"
  | "vectorstore"
  | "retriever"
  | "reranker"
  | "llm"
  | "output";

export interface BrickSpec {
  type: string;
  category: Category;
  emoji: string;
  name: string;
  description: string;
}

// The ordered pipeline stages, with a color per stage for the palette.
export const CATEGORIES: { id: Category; label: string; color: string }[] = [
  { id: "source", label: "📥 Source", color: "#ff5b5b" },
  { id: "chunker", label: "✂️ Chunker", color: "#ff9f43" },
  { id: "embedder", label: "🧬 Embedder", color: "#feca57" },
  { id: "vectorstore", label: "🗄️ Vector Store", color: "#1dd1a1" },
  { id: "retriever", label: "🔎 Retriever", color: "#54a0ff" },
  { id: "reranker", label: "🎚️ Reranker", color: "#5f27cd" },
  { id: "llm", label: "🧠 LLM", color: "#ee5253" },
  { id: "output", label: "📤 Output", color: "#576574" },
];

export const BRICKS: BrickSpec[] = [
  { type: "repo_connector", category: "source", emoji: "📥", name: "Repo Connector", description: "Pull docs & code from your connected repo." },
  { type: "pdf_loader", category: "source", emoji: "📄", name: "PDF Loader", description: "Load a folder of PDFs." },
  { type: "recursive_splitter", category: "chunker", emoji: "✂️", name: "Recursive Splitter", description: "Split on paragraphs, then sentences." },
  { type: "semantic_splitter", category: "chunker", emoji: "🧩", name: "Semantic Splitter", description: "Split where the meaning shifts." },
  { type: "openai_embedder", category: "embedder", emoji: "🧬", name: "OpenAI Embeddings", description: "text-embedding-3 family." },
  { type: "local_embedder", category: "embedder", emoji: "🏠", name: "Local Embeddings", description: "Free, private, runs on your hardware." },
  { type: "chroma_store", category: "vectorstore", emoji: "🗄️", name: "Chroma", description: "Zero-setup local vector store." },
  { type: "pgvector_store", category: "vectorstore", emoji: "🐘", name: "pgvector", description: "Vectors in Postgres. Scales." },
  { type: "similarity_retriever", category: "retriever", emoji: "🔎", name: "Similarity", description: "Top-k nearest vectors." },
  { type: "hybrid_retriever", category: "retriever", emoji: "🪢", name: "Hybrid", description: "Keyword (BM25) + vector." },
  { type: "cross_encoder_reranker", category: "reranker", emoji: "🎚️", name: "Cross-Encoder", description: "Re-score for precision." },
  { type: "claude_llm", category: "llm", emoji: "🧠", name: "Claude", description: "Big context, strong reasoning." },
  { type: "openai_llm", category: "llm", emoji: "🤖", name: "GPT", description: "OpenAI chat models." },
  { type: "cited_answer", category: "output", emoji: "📤", name: "Cited Answer", description: "Answer with inline citations." },
];

export function bricksByCategory(category: Category): BrickSpec[] {
  return BRICKS.filter((b) => b.category === category);
}
