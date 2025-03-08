from infrastructure.task_repository import TaskRepository
from domain.entities import Task

class TaskUseCase:
    def __init__(self):
        self.repository = TaskRepository()

    def add_task(self, task_id, title, description):
        task = Task(task_id, title, description)
        self.repository.add_task(task)

    def list_tasks(self):
        tasks = self.repository.get_all_tasks()
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                print(f"ID: {task.task_id}, Title: {task.title}, Description: {task.description}")

    def remove_task(self, task_id):
        self.repository.remove_task(task_id)
