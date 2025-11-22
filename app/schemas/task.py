from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TarefaCriada(TaskBase):
    pass 

class Tarefa(TaskBase):
    id: int

    class Config:
        from_attributes = True