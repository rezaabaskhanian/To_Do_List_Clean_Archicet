import click
from domain.entitties.entities import Task
from infrastructure.task_repository import TaskRepository
from domain.use_case.task_use_case import TaskUseCase

@click.group()
def cli():
    """My Task Management CLI"""
    pass

@click.command()
@click.argument('task_id', type=int)
@click.argument('title')
@click.argument('description')
def add_task(task_id, title, description):
    """Add a new task"""
    task_use_case = TaskUseCase()
    task_use_case.add_task(task_id, title, description)
    click.echo(f"Task '{title}' added successfully.")

@click.command()
def list_tasks():
    """List all tasks"""
    task_use_case = TaskUseCase()
    task_use_case.list_tasks()

@click.command()
@click.argument('task_id', type=int)
def remove_task(task_id):
    """Remove a task by ID"""
    task_use_case = TaskUseCase()
    task_use_case.remove_task(task_id)
    click.echo(f"Task with ID {task_id} removed successfully.")

# Registering commands with the CLI group
cli.add_command(add_task)
cli.add_command(list_tasks)
cli.add_command(remove_task)

if __name__ == '__main__':
    cli()
