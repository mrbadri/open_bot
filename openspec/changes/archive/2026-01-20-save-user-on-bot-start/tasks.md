## 1. Database Model
- [x] 1.1 Create `backend/src/features/users/models.py` with `BotUser` model
- [x] 1.2 Define fields: `id`, `bale_user_id` (unique), `username`, `first_name`, `last_name`, `is_bot`, `language_code`, `created_at`, `updated_at`
- [x] 1.3 Add proper indexes and constraints

## 2. Database Schema
- [x] 2.1 Create Pydantic schemas in `backend/src/features/users/schemas.py`
- [x] 2.2 Define `BotUserCreate`, `BotUserUpdate`, `BotUserResponse` schemas

## 3. Repository Layer
- [x] 3.1 Create `backend/src/features/users/repository.py`
- [x] 3.2 Implement `get_by_bale_user_id()`, `create()`, `get_or_create()` methods

## 4. Service Layer
- [x] 4.1 Create `backend/src/features/users/service.py`
- [x] 4.2 Implement `save_user_from_message()` method that extracts user data from Bale message and saves it

## 5. Database Migration
- [x] 5.1 Generate Alembic migration for `bot_users` table
- [x] 5.2 Review and test migration up/down

## 6. Bot Integration
- [x] 6.1 Modify `/start` command handler in `bot_service.py` to call user service
- [x] 6.2 Ensure idempotent behavior (don't error if user already exists)
- [x] 6.3 Add proper error handling and logging

## 7. Testing
- [x] 7.1 Write unit tests for user repository
- [x] 7.2 Write unit tests for user service
- [x] 7.3 Write integration test for `/start` command saving user
