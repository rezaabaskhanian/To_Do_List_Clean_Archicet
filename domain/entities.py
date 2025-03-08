class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f"Task({self.task_id}, {self.title}, {self.completed})"