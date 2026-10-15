# TaskFlow API

A RESTful task management API built with FastAPI and PostgreSQL, developed sprint by sprint
as a hands-on backend engineering project.

> **Status:** 🚧 Sprint 2: tasks can be created and listed, and are stored in PostgreSQL.

## Tech Stack

Python 3.13 · FastAPI · PostgreSQL · SQLAlchemy · Alembic · Pytest · Docker Compose · GitHub Actions

## Project Structure

```
taskflow-api/
├── app/
│   ├── core/
│   │   ├── config.py     # Settings from environment / .env
│   │   └── database.py   # Engine, sessions, Base, get_db
│   ├── models/task.py    # Task model (tasks table)
│   └── main.py           # App entry point and routes
├── migrations/versions/  # Alembic migration scripts
├── alembic.ini           # Alembic configuration
├── compose.yaml          # Local PostgreSQL
├── .env.example          # Environment variable template
└── pyproject.toml        # Metadata and dependencies
```

## Getting Started

**Prerequisites:** Python 3.13+, Git, Docker Desktop

```bash
git clone git@github.com:diptoverse/taskflow-api.git
cd taskflow-api
python3.13 -m venv .venv && source .venv/bin/activate
cp .env.example .env          # then set real values (see Configuration)
pip install -e .              # install in editable mode
docker compose up -d          # start PostgreSQL on localhost:5433
alembic upgrade head          # create the tables
uvicorn app.main:app --reload # run the API on http://127.0.0.1:8000
```

## API

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Health check |
| `POST` | `/tasks` | Create a task. Body: `title` (required), `description` (optional) |
| `GET` | `/tasks` | List all tasks, oldest first |

```bash
curl -X POST http://127.0.0.1:8000/tasks -H "Content-Type: application/json" -d '{"title": "Buy milk"}'
curl http://127.0.0.1:8000/tasks
```

Interactive docs: http://127.0.0.1:8000/docs

## Configuration

Set in `.env` (never commit it). Real environment variables override `.env`.

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `TaskFlow API` | Name shown in the API docs |
| `ENVIRONMENT` | `development` | `development`, `test` or `production` |
| `DEBUG` | `false` | Detailed errors and SQL logging. Never in production |
| `DATABASE_URL` | required | e.g. `postgresql+psycopg://taskflow_user:<password>@localhost:5433/taskflow` |
| `POSTGRES_USER` / `POSTGRES_PASSWORD` / `POSTGRES_DB` | required | Used by Docker Compose to create the database on first start |

Use a URL-safe password (`openssl rand -hex 16`) and the same value in `POSTGRES_PASSWORD`
and `DATABASE_URL`.

## Database

- `docker compose down` stops PostgreSQL and keeps data. `docker compose down -v` **deletes all data**.
- After changing a model, create and apply a migration, then commit both together:

```bash
alembic revision --autogenerate -m "describe the change"   # review the new file first
alembic upgrade head
```

## Development Workflow

All changes go through a pull request into `main`.

1. `git switch main && git pull`
2. `git switch -c <type>/<short-description>`
3. Small commits using [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `test:`, `chore:`)
4. `git push -u origin <branch-name>`, open a PR, review, merge
5. `git switch main && git pull`, then delete the branch

## Roadmap

- [x] Sprint 0: Project setup and GitHub
- [x] Sprint 1: FastAPI foundation
- [x] Sprint 2: PostgreSQL and SQLAlchemy
- [ ] Sprint 3: Task CRUD and validation
- [ ] Sprint 4: Authentication
- [ ] Sprint 5: Authorization and ownership
- [ ] Sprint 6: Pagination, filtering and sorting
- [ ] Sprint 7: Testing, logging and error handling
- [ ] Sprint 8: Docker, CI and release readiness
