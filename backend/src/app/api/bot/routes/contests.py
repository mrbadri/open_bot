"""Contest routes for bot API."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_contests():
    """List available contests."""
    # TODO: Implement contest listing logic
    pass


@router.get("/{contest_id}")
async def get_contest(contest_id: int):
    """Get contest details."""
    # TODO: Implement contest retrieval logic
    pass


@router.post("/{contest_id}/participate")
async def participate_in_contest(contest_id: int):
    """Participate in a contest."""
    # TODO: Implement contest participation logic
    pass
