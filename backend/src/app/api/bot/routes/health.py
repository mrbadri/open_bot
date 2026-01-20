"""Health check routes for bot API."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health_check():
    """Bot API health check."""
    return {"status": "healthy", "api": "bot"}
