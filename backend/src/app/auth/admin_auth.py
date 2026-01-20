"""Admin authentication."""

from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


async def verify_admin_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """Verify admin authentication token."""
    token = credentials.credentials
    # TODO: Implement admin token verification
    # For now, raise exception
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Admin authentication not implemented",
    )


async def get_current_admin(
    admin: dict = Depends(verify_admin_token)
) -> dict:
    """Get current admin user."""
    return admin
