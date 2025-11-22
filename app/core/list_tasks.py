from fastapi import APIRouter
from typing import List 
from app.schemas.task import Tarefa
from app.services.task_service import TaskService

router = APIRouter()

@router.get("/", response_model=List[Tarefa])
def list_all_tasks():
    return TaskService.list_tasks()