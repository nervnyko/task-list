from fastapi import FastAPI
from app.core import create_task, list_tasks, delete_task

app = FastAPI(title="Task List API", description="API simples de tarefas", version="1.0.0")

app.include_router(create_task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(list_tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(delete_task.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {
        "message": "API de Tarefas está rodando!",
        "docs": "Acesse /docs para ver a documentação"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)