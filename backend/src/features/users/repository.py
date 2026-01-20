"""Bot user repository."""

from typing import Optional
from sqlalchemy.orm import Session

from features.users.models import BotUser
from features.users.schemas import BotUserCreate


class BotUserRepository:
    """Repository for bot user data access."""

    def __init__(self, db: Session):
        """Initialize repository with database session."""
        self.db = db

    def get_by_bale_user_id(self, bale_user_id: int) -> Optional[BotUser]:
        """Get bot user by Bale user ID."""
        return self.db.query(BotUser).filter(BotUser.bale_user_id == bale_user_id).first()

    def create(self, user_data: BotUserCreate) -> BotUser:
        """Create a new bot user."""
        db_user = BotUser(**user_data.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_or_create(self, user_data: BotUserCreate) -> tuple[BotUser, bool]:
        """
        Get existing bot user or create a new one.
        
        Returns:
            tuple[BotUser, bool]: (user, created) where created is True if user was created
        """
        existing_user = self.get_by_bale_user_id(user_data.bale_user_id)
        if existing_user:
            return existing_user, False
        
        new_user = self.create(user_data)
        return new_user, True
