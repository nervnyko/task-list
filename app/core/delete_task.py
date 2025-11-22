from fastapi import APIRouter, HTTPException
from app.services.task_service import TaskService

router = APIRouter()

@router.delete("/{task_id}", status_code=204)
def remove_task(task_id: int):
    ok = TaskService.delete_task(task_id)
    
    if not ok:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return