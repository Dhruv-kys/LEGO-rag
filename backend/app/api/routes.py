"""🔌 API routes — where the canvas plugs into the brain."""

from fastapi import APIRouter

from app.models.schema import Pipeline, AnalysisReport, GeneratedCode
from app.blocks.registry import REGISTRY, CATEGORIES
from app.analyzer.repo_analyzer import analyze
from app.generator.codegen import generate

router = APIRouter(prefix="/api", tags=["lego-rag"])


@router.get("/bricks")
def list_bricks():
    """The brick catalog — the canvas uses this to fill its palette. 🧱"""
    return {"categories": CATEGORIES, "bricks": REGISTRY}


@router.post("/analyze", response_model=AnalysisReport)
def analyze_pipeline(pipeline: Pipeline):
    """Analyze the connected repo + chosen bricks + constraints. 🔬"""
    return analyze(pipeline)


@router.post("/generate", response_model=GeneratedCode)
def generate_pipeline(pipeline: Pipeline):
    """Compile the snapped-together bricks into runnable RAG code. 🏗️"""
    return generate(pipeline)
