from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Todo API")

# ---------- Schemas ----------
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)

class TaskCreate(TaskBase):
    done: bool = False

class Task(TaskBase):
    id: int
    done: bool

# ---------- In-memory storage ----------
tasks: list[Task] = []
next_id: int = 1

# ---------- Endpoints ----------
@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    global next_id
    new_task = Task(id=next_id, title=payload.title, done=payload.done)
    tasks.append(new_task)
    next_id += 1
    return new_task