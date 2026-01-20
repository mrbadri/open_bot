"""Bot user service."""

from typing import Optional
from sqlalchemy.orm import Session
from telebot import types

from features.users.models import BotUser
from features.users.repository import BotUserRepository
from features.users.schemas import BotUserCreate
from app import logging as app_logging

logger = app_logging.get_logger(__name__)


class BotUserService:
    """Service for bot user business logic."""

    def __init__(self, db: Session):
        """Initialize service with database session."""
        self.repository = BotUserRepository(db)

    def save_user_from_message(self, message: types.Message) -> tuple[Optional[BotUser], bool]:
        """
        Extract user data from Bale message and save to database.
        
        Args:
            message: Bale message object containing user information
            
        Returns:
            tuple[Optional[BotUser], bool]: (user, created) where created is True if user was created.
                                          Returns (None, False) if message.from_user is None.
        """
        if not message.from_user:
            logger.warning("Message has no from_user attribute")
            return None, False

        user = message.from_user

        # Extract user data
        user_data = BotUserCreate(
            bale_user_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            is_bot=user.is_bot if hasattr(user, 'is_bot') else False,
            language_code=user.language_code if hasattr(user, 'language_code') else None,
        )

        try:
            db_user, created = self.repository.get_or_create(user_data)
            
            if created:
                logger.info(
                    f"Created new bot user | bale_user_id={user.id} "
                    f"username={user.username} first_name={user.first_name}"
                )
            else:
                logger.debug(
                    f"Bot user already exists | bale_user_id={user.id}"
                )
            
            return db_user, created
        except Exception as e:
            logger.error(
                f"Error saving bot user | bale_user_id={user.id} error={e}",
                exc_info=True
            )
            raise
