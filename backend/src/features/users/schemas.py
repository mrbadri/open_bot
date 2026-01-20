"""Bot user schemas."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class BotUserBase(BaseModel):
    """Base schema for bot user."""

    bale_user_id: int = Field(..., description="Bale/Telegram user ID")
    username: Optional[str] = Field(None, max_length=255, description="User username")
    first_name: Optional[str] = Field(None, max_length=255, description="User first name")
    last_name: Optional[str] = Field(None, max_length=255, description="User last name")
    is_bot: bool = Field(False, description="Whether the user is a bot")
    language_code: Optional[str] = Field(None, max_length=10, description="User language code")


class BotUserCreate(BotUserBase):
    """Schema for creating a bot user."""

    pass


class BotUserUpdate(BaseModel):
    """Schema for updating a bot user."""

    username: Optional[str] = Field(None, max_length=255, description="User username")
    first_name: Optional[str] = Field(None, max_length=255, description="User first name")
    last_name: Optional[str] = Field(None, max_length=255, description="User last name")
    is_bot: Optional[bool] = Field(None, description="Whether the user is a bot")
    language_code: Optional[str] = Field(None, max_length=10, description="User language code")


class BotUserResponse(BotUserBase):
    """Schema for bot user response."""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="Database ID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
