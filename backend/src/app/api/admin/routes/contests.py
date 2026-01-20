"""Contest management routes for admin API."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_contests():
    """List all contests."""
    # TODO: Implement contest listing logic
    pass


@router.get("/{contest_id}")
async def get_contest(contest_id: int):
    """Get contest details."""
    # TODO: Implement contest retrieval logic
    pass


@router.get("/{contest_id}/results")
async def get_contest_results(contest_id: int):
    """Get contest results."""
    # TODO: Implement contest results retrieval logic
    pass
