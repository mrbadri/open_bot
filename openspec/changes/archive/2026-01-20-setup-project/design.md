# Design: Project Setup

## Context
The project needs to be transformed from a simple single-file bot script into a comprehensive backend system following the architecture specification. This involves establishing the complete project structure, infrastructure, and foundational components.

## Goals / Non-Goals

### Goals
- Establish complete project structure matching architecture.md
- Set up FastAPI application with proper organization
- Configure Docker for both development and production
- Initialize database infrastructure with Alembic
- Create OpenAPI specifications for bot and admin APIs
- Set up all feature modules with proper structure
- Configure logging, error handling, and observability
- Create development tooling and scripts

### Non-Goals
- Implementing business logic (only scaffolding)
- Writing actual feature implementations
- Setting up CI/CD pipelines
- Configuring production deployment infrastructure

## Decisions

### Decision: Use FastAPI as the web framework
**Rationale**: 
- FastAPI provides excellent OpenAPI integration
- Type hints and Pydantic validation align with project conventions
- High performance and modern Python async support
- Good ecosystem and documentation

**Alternatives considered**:
- Django: Too heavyweight, includes ORM we don't need
- Flask: Less modern, weaker OpenAPI support
- Starlette: Too low-level

### Decision: Use SQLAlchemy/SQLModel for ORM
**Rationale**:
- SQLModel provides Pydantic integration with SQLAlchemy
- Type-safe models with validation
- Good migration support via Alembic
- Flexible query building

**Alternatives considered**:
- Django ORM: Tied to Django framework
- Tortoise ORM: Less mature ecosystem
- Raw SQL: Too low-level, error-prone

### Decision: Separate Docker Compose files for dev and prod
**Rationale**:
- Development needs hot-reload, volume mounts, debug tools
- Production needs optimized builds, security hardening, resource limits
- Clear separation prevents production misconfigurations
- Follows project.md conventions

**Alternatives considered**:
- Single docker-compose.yml with profiles: Less clear, harder to maintain
- Environment-based overrides: More complex, harder to reason about

### Decision: Feature-based module organization
**Rationale**:
- Each feature (groups, invites, contests, etc.) is self-contained
- Clear separation of concerns
- Easy to locate and modify feature-specific code
- Scales well as features grow

**Alternatives considered**:
- Layer-based (all models together, all services together): Harder to navigate, tight coupling
- Domain-driven design with aggregates: Over-engineered for current scope

### Decision: OpenAPI-first API design
**Rationale**:
- OpenAPI is source of truth for API contracts
- Enables code generation for clients
- Clear API documentation
- Supports validation and testing

**Alternatives considered**:
- Code-first with auto-generated docs: Less control, harder to maintain contracts
- GraphQL: Doesn't match RESTful API requirements

## Risks / Trade-offs

### Risk: Over-engineering the initial structure
**Mitigation**: Follow architecture.md exactly, avoid adding unnecessary abstractions. Keep it simple until proven insufficient.

### Risk: Missing critical dependencies
**Mitigation**: Review architecture.md thoroughly, check all imports in scaffolded code, validate with requirements.txt.

### Risk: Docker configuration complexity
**Mitigation**: Start with simple configurations, add complexity incrementally. Test both dev and prod setups.

### Risk: Database migration setup issues
**Mitigation**: Follow Alembic best practices, test migrations on clean database, document migration workflow.

## Migration Plan

### Phase 1: Structure Creation
- Create all directories and empty files
- Set up basic configuration files

### Phase 2: Core Infrastructure
- Set up FastAPI app
- Configure database connection
- Set up logging and error handling

### Phase 3: Docker Setup
- Create Dockerfiles
- Configure docker-compose files
- Test container builds

### Phase 4: OpenAPI Setup
- Create OpenAPI specifications
- Validate schema structure

### Phase 5: Feature Scaffolding
- Create all feature module structures
- Set up basic imports and exports

## Open Questions
- Should we include example/test data in the seed script?
- What Python version should we target? (Assume 3.11+)
- Should we set up pre-commit hooks now or later?
