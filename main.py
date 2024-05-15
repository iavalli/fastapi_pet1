from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_task(
    task: STaskAdd,
):
    tasks.append(task)
    return {"ok": True}


    
"""
@app.get("/tasks")
def get_task():
    task = Task(name="Buy bread")
    return {"data": task}
"""
