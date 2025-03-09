import json
from domain.entitties.entities import Task

class TaskRepository:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            self.tasks = []

    def get_all_tasks(self):
        return self.tasks

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_file()

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_to_file()
