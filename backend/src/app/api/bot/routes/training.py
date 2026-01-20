"""Training content routes for bot API."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_training_content():
    """List training content."""
    # TODO: Implement training content listing logic
    pass


@router.get("/{content_id}")
async def get_training_content(content_id: int):
    """Get training content details."""
    # TODO: Implement training content retrieval logic
    pass
