## 1. Cleanup
- [x] 1.1 Delete unused template directory `backend/src/features/contests/{scoring}/` and its contents
- [x] 1.2 Delete duplicate unused `backend/docker/` directory and all its contents
- [x] 1.3 Delete unused `backend/openapi/` directory and all its contents (FastAPI auto-generates OpenAPI)
- [x] 1.4 Remove or update `backend/scripts/generate_openapi_clients.sh` script (references removed openapi directory)

## 2. Documentation Consolidation
- [x] 2.1 Create consolidated `backend/DOCUMENTATION.md` file with essential information from:
  - Docker setup and usage (from DOCKER.md)
  - Docker migrations (from DOCKER_MIGRATIONS.md)
  - Database migrations (from MIGRATIONS.md)
  - Local development setup (from DEVELOPMENT.md)
- [x] 2.2 Update `backend/README.md` to reference `DOCUMENTATION.md` instead of individual files
- [x] 2.3 Delete redundant documentation files:
  - `backend/DOCKER.md`
  - `backend/DOCKER_MIGRATIONS.md`
  - `backend/MIGRATIONS.md`
  - `backend/DEVELOPMENT.md`
