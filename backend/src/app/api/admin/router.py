"""Admin API router."""

from fastapi import APIRouter

from app.api.admin.routes import (
    auth,
    groups,
    leaders,
    members,
    invites,
    contests,
    exports,
    audit,
    users,
)

router = APIRouter()

# Register route modules
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(groups.router, prefix="/groups", tags=["groups"])
router.include_router(leaders.router, prefix="/leaders", tags=["leaders"])
router.include_router(members.router, prefix="/members", tags=["members"])
router.include_router(invites.router, prefix="/invites", tags=["invites"])
router.include_router(contests.router, prefix="/contests", tags=["contests"])
router.include_router(exports.router, prefix="/exports", tags=["exports"])
router.include_router(audit.router, prefix="/audit", tags=["audit"])
router.include_router(users.router, prefix="/users", tags=["users"])
