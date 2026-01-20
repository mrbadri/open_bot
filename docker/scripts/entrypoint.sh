#!/bin/bash
set -e

# Wait for database to be ready
if [ -n "$DATABASE_URL" ]; then
    echo "Waiting for database..."
    /docker-scripts/wait_for_db.sh
fi

# Run database migrations
echo "Running database migrations..."
cd /app/src/app/db/migrations && alembic upgrade head || echo "Migrations failed or no migrations to run"

# Execute the main command
exec "$@"
