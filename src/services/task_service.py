# In-memory list to store tasks.
from db import db
from models.task import Task

tasks = []

def add_task(data):
    """Add a new task to the list and return the created task."""
    new_task = {
        "id": len(tasks) + 1,
        "task": data['task'],
        "due_by": data['due_by']
    }
    tasks.append(new_task)
    return new_task

def list_tasks():
    """Return the list of all tasks."""
    tasks_from_db = db.session.execute(db.select(Task)).scalars()
    t = [ta.task for ta in tasks_from_db]
    return t
