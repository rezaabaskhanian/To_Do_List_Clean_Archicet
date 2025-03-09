# main.py
from domain.use_case.task_use_case import TaskUseCase

def main():
    task_use_case = TaskUseCase()
    task_use_case.add_task(1, "Learn Python", "Learn the basics of Python programming.")
    task_use_case.add_task(2, "Do Homework", "Complete math homework.")

    task_use_case.list_tasks()
    # task_use_case.remove_task(1)
    # task_use_case.list_tasks()

if __name__ == "__main__":
    main()
