## ADDED Requirements

### Requirement: Bot Command Handling
The system SHALL process and respond to bot commands sent by users through the Bale messaging platform.

#### Scenario: Start command response
- **WHEN** a user sends `/start` command to the bot
- **THEN** the bot responds with a greeting message

#### Scenario: Echo command response
- **WHEN** a user sends `/echo <text>` command to the bot
- **THEN** the bot responds with the provided text, or a usage message if no text is provided

#### Scenario: Unknown command handling
- **WHEN** a user sends an unrecognized command to the bot
- **THEN** the bot handles the error gracefully without crashing

### Requirement: Bot Service Lifecycle
The bot service SHALL start automatically when the application starts and shut down gracefully when the application stops.

#### Scenario: Bot starts with application
- **WHEN** the FastAPI application starts
- **THEN** the bot service initializes and begins polling for messages

#### Scenario: Bot shuts down gracefully
- **WHEN** the application receives a shutdown signal
- **THEN** the bot service stops polling and closes connections cleanly

### Requirement: Bot Configuration
The bot SHALL use configuration from environment variables and application settings.

#### Scenario: Bot uses token from settings
- **WHEN** the bot service initializes
- **THEN** it uses the `BALE_BOT_TOKEN` from application settings

#### Scenario: Bot uses API URL from settings
- **WHEN** the bot service initializes
- **THEN** it uses the `BALE_API_URL` from application settings (defaults to Bale API endpoint)
