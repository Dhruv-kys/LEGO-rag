"""📐 The wire format.

These models describe what the canvas sends to the brain: the bricks the user
snapped together, how they're connected, and what they care about (cost,
memory, domain, ...). Keep this in sync with the frontend types.
"""

from typing import Any, Optional
from pydantic import BaseModel, Field


class Brick(BaseModel):
    """A single LEGO brick on the canvas (one stage of the RAG pipeline)."""

    id: str = Field(..., description="Unique id of this brick on the canvas")
    category: str = Field(..., description="e.g. 'source', 'chunker', 'embedder'")
    type: str = Field(..., description="The specific brick, e.g. 'recursive_splitter'")
    config: dict[str, Any] = Field(default_factory=dict, description="Brick settings")


class Connection(BaseModel):
    """A stud-to-hole link between two bricks."""

    source: str = Field(..., description="id of the upstream brick")
    target: str = Field(..., description="id of the downstream brick")


class Constraints(BaseModel):
    """What the builder is optimizing for. Steers brick recommendations."""

    domain: Optional[str] = Field(None, description="e.g. 'legal', 'code', 'medical'")
    optimize_for: list[str] = Field(
        default_factory=list,
        description="any of: production, scalability, cost, memory, context_tokens",
    )
    monthly_queries: Optional[int] = None


class Pipeline(BaseModel):
    """A full build: the bricks, their wiring, and the builder's intent."""

    bricks: list[Brick] = Field(default_factory=list)
    connections: list[Connection] = Field(default_factory=list)
    constraints: Constraints = Field(default_factory=Constraints)
    repo_url: Optional[str] = Field(None, description="The connected repository")


class AnalysisReport(BaseModel):
    """What the brain hands back to the canvas."""

    summary: str
    recommended_bricks: list[str] = Field(default_factory=list)
    estimated_cost_per_1k: Optional[float] = None
    estimated_memory_mb: Optional[float] = None
    warnings: list[str] = Field(default_factory=list)


class GeneratedCode(BaseModel):
    """The runnable pipeline assembled from the bricks."""

    language: str = "python"
    files: dict[str, str] = Field(
        default_factory=dict, description="filename -> file contents"
    )
