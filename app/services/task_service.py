from app.schemas.task import TarefaCriada, Tarefa

mentirinha_db = []

#cria
class TaskService:
    @staticmethod
    def create_task(task_in: TarefaCriada) -> Tarefa:
        new_id = len(mentirinha_db) + 1
        
        task_data = task_in.dict()
        task_data['id'] = new_id
        
        nova_tarefa = Tarefa(**task_data)
        
        mentirinha_db.append(nova_tarefa)
        return nova_tarefa

#delete
    @staticmethod
    def delete_task(task_id: int) -> bool:
        for index, task in enumerate(mentirinha_db):
            if task.id == task_id:
                del mentirinha_db[index]
                return True
            
            return False
#listar
    @staticmethod
    def list_tasks():
        return mentirinha_db