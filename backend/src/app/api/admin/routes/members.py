"""Member management routes for admin API."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_members():
    """List all members."""
    # TODO: Implement member listing logic
    pass


@router.get("/{member_id}")
async def get_member(member_id: int):
    """Get member details."""
    # TODO: Implement member retrieval logic
    pass
