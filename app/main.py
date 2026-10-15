from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.models import Task

app = FastAPI(title=settings.app_name)


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


def task_to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "is_completed": task.is_completed,
        "created_at": task.created_at,
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.environment}


@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)) -> dict:
    task = Task(title=payload.title, description=payload.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task_to_dict(task)


@app.get("/tasks")
def list_tasks(db: Session = Depends(get_db)) -> list[dict]:
    tasks = db.scalars(select(Task).order_by(Task.id)).all()
    return [task_to_dict(task) for task in tasks]
