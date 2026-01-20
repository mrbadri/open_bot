# Project Context

## Purpose
This project is a backend system for a Bale messenger bot (Telegram-compatible API).
The system manages groups, leaders, subgroups, phone-based invite links, training content, and leader-only contests.

Users interact with the system only through invite links and phone-number verification.
A Super Admin panel is provided for system-wide control, monitoring, and data access.

The backend is designed using OpenAPI (OpenSpec) to enable code generation and clear API contracts.

Primary goals:
- Phone-based authorization and identity
- Invite-only join flow via secure links
- Role-based access control
- Contest lifecycle management
- Admin-level observability and reporting
- Bot-first interaction model

---

## Tech Stack
- Backend: Python (framework-agnostic, API-first)
- Web Framework: FastAPI
- ORM: SQLAlchemy / SQLModel
- Database Migrations: Alembic
- Data Validation: Pydantic
- API Specification: OpenAPI 3.x (YAML)
- Database: PostgreSQL
- Bot Platform: Bale (Telegram-compatible Bot API)
- Admin Panel: Web-based dashboard (read/write, role-protected)
- Containerization: Docker
- Orchestration: Docker Compose (separate configs for dev and production)
- Auth Model:
  - Bot users: phone-based headers
  - Admins: secure admin authentication (separate from bot users)

---

## Project Conventions

### Code Style
- Explicit, readable naming (no abbreviations)
- snake_case for database fields
- camelCase for API payloads
- Controllers are thin; business logic lives in services
- Validation before persistence
- All errors must be explicit and structured

### Architecture Patterns
- API-first (OpenAPI is the source of truth)
- Layered architecture:
  - Controller
  - Service
  - Repository
- Stateless backend
- Invite-driven authorization
- Admin APIs separated from Bot APIs

### Testing Strategy
- Unit tests for business logic (services)
- Integration tests for critical flows:
  - Invite creation & acceptance
  - Phone mismatch rejection
  - Contest lifecycle
  - Admin data access
- No UI tests required for bot flows

### Git Workflow
- main: stable
- feature/*: new features
- fix/*: bug fixes
- Commits follow conventional commits:
  - feat, fix, refactor, docs
- PRs must document:
  - Business flow impact
  - API changes
  - Data model changes

---

## Domain Context

### Groups
- Unlimited number of groups
- Each group may contain multiple subgroups
- Each group has one or more leaders

### Leaders
- Pre-approved via phone number
- Can:
  - Manage subgroups
  - Create invite links
  - Access leader-only training
  - Create and manage contests

### Members
- Join only via invite link
- Phone number must match invite
- Can participate in contests (if allowed)
- Cannot create contests

### Invites
- Link-based only
- Bound to a specific phone number
- Single-use and expirable
- Role is assigned at creation time

---

## Contest Definition

### Contest Purpose
Contests are used to motivate leaders or members through competitive activities such as quizzes, performance tracking, or participation-based scoring.

### Contest Roles
- Only leaders (or assistant leaders) can create and manage contests
- Members can only participate

### Contest Lifecycle
- Draft: created but not visible
- Scheduled: has start and end time
- Active: within the active time window
- Finished: ended and results finalized

### Contest Types (Examples)
- Individual score-based contests
- Subgroup-based competitions
- Activity or participation tracking contests

### Contest Rules
- Contests are associated with exactly one group
- Editing is allowed only before the contest becomes active
- Scoring logic is configurable per contest
- Results are computed and stored
- Results can be published to the bot

### Contest Data
- Title, description
- Start and end timestamps
- Visibility (leaders-only or all members)
- Rules and scoring configuration
- Results (rank, score, metadata)

---

## Super Admin Panel

### Purpose
The Super Admin panel provides full visibility and control over the entire system.

### Capabilities
- View and manage all groups
- View and manage leaders and members
- Approve or reject leader registrations
- Monitor invite usage and abuse
- View contest statistics and results
- Export data (CSV/JSON)
- System-wide analytics and reporting

### Access Control
- Super Admin access is separate from bot users
- Protected by strong authentication
- Full read/write permissions

### Admin Data Visibility
- Group-level metrics
- Leader performance
- Member participation
- Contest engagement and outcomes
- Invite creation and usage history

---

## Important Constraints
- No user can join without a valid invite link
- Phone number must be verified via share
- Invite phone mismatch must be rejected
- Roles cannot be self-assigned
- Contest rules cannot change after start
- Admin APIs must not be exposed to bot users

---

## Docker & Deployment

### Dockerization
The project must be fully dockerized to ensure consistent environments across development and production.

### Docker Compose Configuration
Two separate docker-compose files are maintained:

#### Development Mode (`docker-compose.dev.yml`)
- Hot-reload enabled for code changes
- Development database with seed data
- Debug logging enabled
- Volume mounts for live code editing
- Optional development tools (debuggers, profilers)
- Relaxed security settings for local development

#### Production Mode (`docker-compose.prod.yml`)
- Optimized production builds
- Production database configuration
- Logging configured for production monitoring
- No volume mounts (code baked into images)
- Security hardening enabled
- Resource limits and health checks configured
- Environment variables from secure sources

### Docker Requirements
- All services must be containerized (backend, database, admin panel if applicable)
- Dockerfiles must follow best practices (multi-stage builds, minimal base images)
- Images should be tagged appropriately for versioning
- Health checks must be implemented for all services
- Secrets management via environment variables or Docker secrets

### Deployment Strategy
- Development: Use `docker-compose.dev.yml` for local development
- Production: Use `docker-compose.prod.yml` for production deployments
- Both configurations should share common service definitions where possible
- Production builds should be optimized for size and security

---

## External Dependencies
- Bale Bot API (Telegram-compatible)
- Phone number sharing via Bale client
- Admin authentication provider (TBD)
- Data export tooling
