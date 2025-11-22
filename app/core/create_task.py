from fastapi import HTTPException, APIRouter
from app.schemas.task import TarefaCriada, Tarefa
from app.services.task_service import TaskService


router = APIRouter ()

@router.post ("/", response_model=Tarefa)
def create_task (task: TarefaCriada):
    return TaskService.create_task(task)