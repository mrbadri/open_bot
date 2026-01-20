# Change: Add Bot Command Handling and Docker Integration

## Why
The bot currently exists as a standalone script (`bot.py`) that is not integrated with the Docker infrastructure or the FastAPI application. Users need to manually run the bot separately, which creates deployment complexity and prevents the bot from starting automatically when the application or Docker containers start. This change integrates the bot into the application lifecycle and enables automatic startup with Docker.

## What Changes
- Add bot command handling capability to process user commands
- Integrate bot service into Docker Compose configurations (dev and production)
- Create bot service module that starts automatically with the application
- Move bot logic from standalone `bot.py` into the backend application structure
- Configure bot to use environment variables for token and settings
- Add bot service to Docker Compose with proper dependencies and health checks

## Impact
- Affected specs: 
  - `bot-commands` (new capability)
  - `project-setup` (modified to include bot service)
- Affected code:
  - `bot.py` (will be refactored into backend structure)
  - `docker/docker-compose.dev.yml` (add bot service)
  - `docker/docker-compose.prod.yml` (add bot service)
  - `backend/src/integrations/bale/` (add bot service implementation)
  - `backend/src/app/main.py` (integrate bot startup)
  - `docker/Dockerfile` (may need updates for bot dependencies)
