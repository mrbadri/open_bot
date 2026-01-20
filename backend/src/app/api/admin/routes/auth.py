"""Admin authentication routes."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login():
    """Admin login."""
    # TODO: Implement admin authentication logic
    pass


@router.post("/logout")
async def logout():
    """Admin logout."""
    # TODO: Implement admin logout logic
    pass


@router.get("/me")
async def get_current_admin():
    """Get current admin user."""
    # TODO: Implement current admin retrieval logic
    pass
