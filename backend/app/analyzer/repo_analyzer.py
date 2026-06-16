"""🔬 Repo analyzer (boilerplate).

The whole point of connecting your *actual* repo is that we can recommend
bricks for *your* data instead of a generic tutorial. This module is where that
analysis will live: peek at the repo, size up the corpus, sniff the domain,
then suggest a brick set that fits the builder's constraints.

For now it returns a friendly canned report. Wire in real repo inspection later.
"""

from app.models.schema import Pipeline, AnalysisReport
from app.blocks.registry import bricks_by_category


def analyze(pipeline: Pipeline) -> AnalysisReport:
    """Analyze the connected repo + chosen bricks + constraints.

    TODO:
      - clone / read the repo at `pipeline.repo_url`
      - estimate corpus size (docs, tokens) -> drives chunker & store choice
      - detect domain (code? legal? prose?) -> drives embedder & LLM choice
      - turn `constraints.optimize_for` into concrete cost/memory math
    """
    optimize = pipeline.constraints.optimize_for or ["production"]

    recommended: list[str] = []
    recommended += bricks_by_category("source")[:1]
    recommended += ["recursive_splitter"]
    # Cost-sensitive builders get the free, local embedder.
    recommended += ["local_embedder" if "cost" in optimize else "openai_embedder"]
    # Scale-sensitive builders get the database-backed store.
    recommended += ["pgvector_store" if "scalability" in optimize else "chroma_store"]
    recommended += ["similarity_retriever", "claude_llm", "cited_answer"]

    warnings: list[str] = []
    if not pipeline.repo_url:
        warnings.append("No repo connected — recommendations are generic. 🔌")
    if not any(b.category == "llm" for b in pipeline.bricks):
        warnings.append("No 🧠 LLM brick on the canvas yet.")

    return AnalysisReport(
        summary=(
            f"Analyzed {len(pipeline.bricks)} brick(s), optimizing for "
            f"{', '.join(optimize)}. Here's a starter build. 🧱"
        ),
        recommended_bricks=recommended,
        estimated_cost_per_1k=0.0 if "cost" in optimize else 1.20,  # placeholder $
        estimated_memory_mb=512.0,  # placeholder
        warnings=warnings,
    )
