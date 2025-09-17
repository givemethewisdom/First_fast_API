from typing import Annotated

from repository import TaskRepository
from shemas import STaskAdd, STask, STaskId
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/tasks",
    tags=['тэги'],
)

@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],# чтобы были красивые рамки
)-> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks