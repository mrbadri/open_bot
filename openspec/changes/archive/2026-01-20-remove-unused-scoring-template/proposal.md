# Change: Remove Unused Template, Duplicate, and Extra Directories

## Why
During project setup, several unused directories were created that are not being used:
1. A template directory `backend/src/features/contests/{scoring}/` was created but never properly replaced with the actual `scoring` directory
2. A duplicate `backend/docker/` directory exists, but the project uses `docker/` at the root level (as configured in Makefile and all documentation)
3. The `backend/openapi/` directory contains manually written OpenAPI YAML files, but FastAPI auto-generates OpenAPI schema from code. These files are not loaded by the application and are only referenced by a client generation script that may not be actively used.

These unused directories create confusion and should be removed to keep the codebase clean.

## What Changes
- Remove unused template directory `backend/src/features/contests/{scoring}/` and its empty `__init__.py` file
- Remove duplicate unused `backend/docker/` directory and all its contents (Dockerfile, docker-compose files, scripts)
- Remove unused `backend/openapi/` directory and all its contents (bot.openapi.yml, admin.openapi.yml, components/)
- Remove or update `backend/scripts/generate_openapi_clients.sh` script since it references the removed openapi directory
- Consolidate documentation: Create a single `backend/DOCUMENTATION.md` summary file that combines essential information from `DOCKER.md`, `DOCKER_MIGRATIONS.md`, `MIGRATIONS.md`, and `DEVELOPMENT.md`
- Remove redundant documentation files: `backend/DOCKER.md`, `backend/DOCKER_MIGRATIONS.md`, `backend/MIGRATIONS.md`, `backend/DEVELOPMENT.md`
- Update `backend/README.md` to reference the new consolidated `DOCUMENTATION.md` file
- No code changes required - this is a cleanup operation

## Impact
- Affected specs: `project-setup` (project structure requirement)
- Affected code: Removal of unused directories, documentation consolidation, and potentially the client generation script
- Documentation: Multiple MD files consolidated into a single `DOCUMENTATION.md` for easier maintenance
- No breaking changes - these directories are not referenced by the application code
- The active `docker/` directory at root level remains unchanged
- FastAPI will continue to auto-generate OpenAPI schema at `/docs` and `/openapi.json`
