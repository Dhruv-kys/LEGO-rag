"""🏗️ Code generator (boilerplate).

This is the magic the README promises: the bricks the user snapped together get
compiled into real, runnable RAG code. Right now it emits a single,
clearly-marked stub file so the round-trip works end to end. Replace the
templates with real per-brick code as the catalog matures.
"""

from app.models.schema import Pipeline, GeneratedCode
from app.blocks.registry import get_brick


def _pipeline_comment(pipeline: Pipeline) -> str:
    """Render the brick wiring as a human-readable comment."""
    lines = ["# 🧱 Pipeline assembled from your bricks:"]
    for brick in pipeline.bricks:
        spec = get_brick(brick.type) or {}
        emoji = spec.get("emoji", "🔲")
        name = spec.get("name", brick.type)
        lines.append(f"#   {emoji} {name}  ({brick.category})  cfg={brick.config}")
    if not pipeline.bricks:
        lines.append("#   (no bricks on the canvas yet)")
    return "\n".join(lines)


def generate(pipeline: Pipeline) -> GeneratedCode:
    """Turn a brick pipeline into runnable code.

    TODO:
      - topologically sort bricks by their connections
      - emit a real code block per brick from templates
      - render requirements.txt from the chosen bricks
    """
    pipeline_comment = _pipeline_comment(pipeline)

    rag_py = f'''"""Auto-generated RAG pipeline — built with 🧱 LEGO RAG.

This is a boilerplate stub. As the brick templates land, each brick below will
expand into real load / chunk / embed / store / retrieve / answer code.
"""

{pipeline_comment}


def build_pipeline():
    """Assemble the RAG pipeline from the bricks above."""
    # TODO: instantiate each brick in connection order.
    raise NotImplementedError("Snap in real brick templates to bring me to life. 🧱")


def query(question: str) -> str:
    """Ask the assembled pipeline a question."""
    # TODO: retrieve -> (rerank) -> stuff context -> call LLM -> format output.
    raise NotImplementedError("Connect the 🧠 LLM brick to answer questions.")


if __name__ == "__main__":
    print("🧱 This RAG was built with LEGO RAG. Fill in the bricks to run it.")
'''

    return GeneratedCode(language="python", files={"rag_pipeline.py": rag_py})
