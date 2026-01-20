# Change: Save User in Database on Bot Start

## Why
When users interact with the bot for the first time via the `/start` command, we need to persist their information in the database. This enables:
- Tracking user interactions and engagement
- Building user profiles for future features (contests, training, etc.)
- Supporting admin panel user management and analytics
- Enabling user-specific features and personalization

Currently, the bot only logs user interactions but doesn't store user data, which limits our ability to build user-centric features.

## What Changes
- Create a `BotUser` database model to store user information from Bale/Telegram API
- Add user repository and service following the existing architecture patterns
- Modify the `/start` command handler to save users on first interaction (idempotent - only saves if user doesn't exist)
- Create database migration for the new `bot_users` table
- Update bot-commands specification to include user persistence requirement

## Impact
- Affected specs: `bot-commands`
- Affected code:
  - `backend/src/integrations/bale/bot_service.py` - Modify `/start` handler
  - `backend/src/features/users/` - New feature module (models, schemas, repository, service)
  - `backend/src/app/db/migrations/` - New migration file
- Database: New `bot_users` table
