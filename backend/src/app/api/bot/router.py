"""Bot API router."""

from fastapi import APIRouter

from app.api.bot.routes import (
    invites,
    phone_verification,
    contests,
    training,
    health,
)

router = APIRouter()

# Register route modules
router.include_router(invites.router, prefix="/invites", tags=["invites"])
router.include_router(
    phone_verification.router, prefix="/phone", tags=["phone"]
)
router.include_router(contests.router, prefix="/contests", tags=["contests"])
router.include_router(training.router, prefix="/training", tags=["training"])
router.include_router(health.router, prefix="/health", tags=["health"])
