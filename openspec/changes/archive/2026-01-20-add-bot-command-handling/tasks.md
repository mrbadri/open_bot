## 1. Bot Command Handling Implementation
- [x] 1.1 Create bot service module in `backend/src/integrations/bale/bot_service.py`
- [x] 1.2 Implement command handler registration system
- [x] 1.3 Implement `/start` command handler
- [x] 1.4 Implement `/echo` command handler (migrate from existing bot.py)
- [x] 1.5 Add error handling and logging for bot operations
- [x] 1.6 Configure bot to use settings from environment variables

## 2. Application Integration
- [x] 2.1 Create bot lifecycle manager (startup/shutdown hooks)
- [x] 2.2 Integrate bot startup into FastAPI application lifecycle
- [x] 2.3 Add bot health check endpoint or monitoring
- [x] 2.4 Update `backend/src/app/main.py` to initialize bot service

## 3. Docker Integration
- [x] 3.1 Add bot service to `docker/docker-compose.dev.yml`
- [x] 3.2 Add bot service to `docker/docker-compose.prod.yml`
- [x] 3.3 Configure bot service dependencies (wait for backend/database if needed)
- [x] 3.4 Add environment variables for bot token and configuration
- [x] 3.5 Add health check for bot service
- [x] 3.6 Update Dockerfile if needed for bot dependencies

## 4. Configuration and Settings
- [x] 4.1 Ensure `BALE_BOT_TOKEN` is configured in environment variables
- [x] 4.2 Update settings validation to require bot token
- [x] 4.3 Document bot configuration in README or development docs

## 5. Testing and Validation
- [x] 5.1 Test bot starts automatically with Docker Compose
- [x] 5.2 Test bot commands work correctly (`/start`, `/echo`)
- [x] 5.3 Verify bot restarts properly on container restart
- [x] 5.4 Test bot handles errors gracefully

**Testing Documentation:**
- Created `BOT_TESTING.md` with comprehensive testing guide
- Created `BOT_DEBUGGING.md` with troubleshooting guide
- Bot status endpoint available at `/bot/status`
- Big status prints added for easy visibility in logs

## 6. Cleanup
- [x] 6.1 Remove or archive standalone `bot.py` file (or document migration)
  - Migrated to `bot.py.migrated` with migration notes
  - Original functionality moved to `backend/src/integrations/bale/bot_service.py`
- [x] 6.2 Update documentation to reflect new bot integration
  - Updated `backend/README.md` with bot service section
  - Updated `backend/DEVELOPMENT.md` with bot configuration
  - Created comprehensive testing and debugging guides
