"""Bot user models."""

from datetime import datetime
from sqlalchemy import BigInteger, String, Boolean, DateTime, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from common.time import now


class BotUser(Base):
    """Bot user model for storing Bale/Telegram user information."""

    __tablename__ = "bot_users"

    # Primary key
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # Bale/Telegram user ID (unique identifier from Bale API)
    bale_user_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)

    # User profile information
    username: Mapped[str | None] = mapped_column(String(255), nullable=True)
    first_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_bot: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    language_code: Mapped[str | None] = mapped_column(String(10), nullable=True)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=now)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=now, onupdate=now)
