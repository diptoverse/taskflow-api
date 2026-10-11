# TaskFlow API

A RESTful task management API built with FastAPI and PostgreSQL.

Users will be able to register, log in, and manage their own tasks, with
pagination, filtering, and sorting. This project is built incrementally in
sprints as a hands-on backend engineering exercise.

> **Status:** 🚧 Sprint 0: project setup. No application code yet.

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
├── app/              # Application code
├── tests/            # Automated tests
├── .env.example      # Template for environment variables
├── pyproject.toml    # Project metadata and dependencies
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

Instructions for installing dependencies and running the API will be added in Sprint 1.

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
- [ ] Sprint 1: FastAPI foundation
- [ ] Sprint 2: PostgreSQL and SQLAlchemy
- [ ] Sprint 3: Task CRUD and validation
- [ ] Sprint 4: Authentication
- [ ] Sprint 5: Authorization and ownership
- [ ] Sprint 6: Pagination, filtering and sorting
- [ ] Sprint 7: Testing, logging and error handling
- [ ] Sprint 8: Docker, CI and release readiness
