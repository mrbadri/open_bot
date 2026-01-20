"""Audit log routes for admin API."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_audit_logs():
    """List audit logs."""
    # TODO: Implement audit log listing logic
    pass


@router.get("/{log_id}")
async def get_audit_log(log_id: int):
    """Get audit log details."""
    # TODO: Implement audit log retrieval logic
    pass
