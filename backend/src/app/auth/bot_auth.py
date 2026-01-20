"""Bot user authentication."""

from typing import Optional
from fastapi import Header, HTTPException, status


async def verify_phone_header(
    x_phone_number: Optional[str] = Header(None, alias="X-Phone-Number")
) -> str:
    """Verify phone number from header."""
    if not x_phone_number:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Phone number required",
        )
    # TODO: Implement phone number validation
    return x_phone_number


async def get_current_user_phone(
    phone: str = Header(..., alias="X-Phone-Number")
) -> str:
    """Get current user's phone number."""
    # TODO: Implement user lookup and validation
    return phone
