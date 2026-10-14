# TaskFlow API

A RESTful task management API built with FastAPI and PostgreSQL.

Users will be able to register, log in, and manage their own tasks, with
pagination, filtering, and sorting. This project is built incrementally in
sprints as a hands-on backend engineering exercise.

> **Status:** 🚧 Sprint 1: FastAPI foundation. The API runs locally with a health check endpoint.

## Tech Stack

| Layer            | Technology            |
|------------------|-----------------------|
| Language         | Python 3.13           |
| Web framework    | FastAPI               |
| Database         | PostgreSQL            |
| ORM              | SQLAlchemy            |
| Migrations       | Alembic               |
| Testing          | Pytest                |
| Containerization | Docker, Docker Compose |
| CI               | GitHub Actions        |

## Project Structure

```
taskflow-api/
├── app/
│   ├── core/
│   │   └── config.py   # Settings loaded from environment / .env
│   └── main.py         # FastAPI app entry point
├── tests/              # Automated tests
├── .env.example        # Template for environment variables
├── pyproject.toml      # Project metadata and dependencies
└── README.md
```


## Getting Started

### Prerequisites

- Python 3.13+
- Git

### Setup

1. **Clone the repository**

   ```bash
   git clone git@github.com:diptoverse/taskflow-api.git
   cd taskflow-api
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

3. **Create your local environment file**

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and replace the placeholder values. Never commit `.env`.

4. **Install the project and its dependencies**

   ```bash
   pip install -e .
   ```

   `-e` installs in editable mode, so code changes apply without reinstalling.

### Run the API

```bash
uvicorn app.main:app --reload
```

The API is available at http://127.0.0.1:8000. `--reload` restarts the server on file changes (development only).

Check that it is running:

```bash
curl http://127.0.0.1:8000/health
# {"status":"ok","environment":"development"}
```

### API Documentation

FastAPI generates interactive documentation automatically:

| URL | Description |
|-----|-------------|
| http://127.0.0.1:8000/docs | Swagger UI: try endpoints in the browser |
| http://127.0.0.1:8000/redoc | ReDoc: read-only reference |
| http://127.0.0.1:8000/openapi.json | Raw OpenAPI specification |

## Configuration

Settings are read from environment variables, falling back to `.env`, then to defaults
(see `app/core/config.py`). Real environment variables take priority over `.env`.

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `TaskFlow API` | Name shown in the API docs |
| `ENVIRONMENT` | `development` | One of `development`, `test`, `production` |
| `DEBUG` | `false` | Detailed error output. Never enable in production |


## Development Workflow

All changes go through a pull request. Nothing is committed directly to `main`.

1. Update `main`: `git switch main && git pull`
2. Create a branch: `git switch -c <type>/<short-description>`
3. Make small, focused commits using [Conventional Commits](https://www.conventionalcommits.org/)
   (`feat:`, `fix:`, `docs:`, `test:`, `chore:`)
4. Push the branch: `git push -u origin <branch-name>`
5. Open a pull request into `main`, review it, and merge
6. Sync locally: `git switch main && git pull`, then delete the branch


## Roadmap

- [x] Sprint 0: Project setup and GitHub
- [x] Sprint 1: FastAPI foundation
- [ ] Sprint 2: PostgreSQL and SQLAlchemy
- [ ] Sprint 3: Task CRUD and validation
- [ ] Sprint 4: Authentication
- [ ] Sprint 5: Authorization and ownership
- [ ] Sprint 6: Pagination, filtering and sorting
- [ ] Sprint 7: Testing, logging and error handling
- [ ] Sprint 8: Docker, CI and release readiness
