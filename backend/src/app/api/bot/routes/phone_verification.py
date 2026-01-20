"""Phone verification routes for bot API."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/verify")
async def verify_phone():
    """Verify phone number."""
    # TODO: Implement phone verification logic
    pass
