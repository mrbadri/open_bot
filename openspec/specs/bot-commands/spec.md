# bot-commands Specification

## Purpose
TBD - created by archiving change add-bot-command-handling. Update Purpose after archive.
## Requirements
### Requirement: Bot Command Handling
The system SHALL process and respond to bot commands sent by users through the Bale messaging platform.

#### Scenario: Start command response
- **WHEN** a user sends `/start` command to the bot
- **THEN** the bot responds with a greeting message

#### Scenario: Start command saves user
- **WHEN** a user sends `/start` command to the bot for the first time
- **THEN** the user information is saved to the database with their Bale user ID, username, first name, and other available profile data

#### Scenario: Start command handles existing user
- **WHEN** a user sends `/start` command to the bot and the user already exists in the database
- **THEN** the bot responds with a greeting message without creating a duplicate user record

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

### Requirement: User Persistence
The system SHALL persist user information when users interact with the bot for the first time.

#### Scenario: User saved on first interaction
- **WHEN** a user sends `/start` command and the user does not exist in the database
- **THEN** a new `BotUser` record is created with the user's Bale user ID, username, first name, last name, and other available profile fields from the message

#### Scenario: User data is complete
- **WHEN** a user is saved to the database
- **THEN** the user record includes at minimum: Bale user ID (unique identifier), username (if available), first name (if available), and timestamps for creation and last update

#### Scenario: User lookup by Bale ID
- **WHEN** querying for a user by their Bale user ID
- **THEN** the system returns the user record if it exists, or None if the user has not interacted with the bot

