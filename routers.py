from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import STaskAdd, STask, STaskId
from repository import TaskRepo


router = APIRouter(prefix="/tasks",
                   tags=["Task Checker"])


@router.post("")
async def add_tasks(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepo.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepo.find_all()
    return tasks