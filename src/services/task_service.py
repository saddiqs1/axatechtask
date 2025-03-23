import logging
from db import db
from models.task import Task, TaskSchema
from dto.task import TaskCreationSchema

task_schema = TaskSchema()
task_creation_schema = TaskCreationSchema()

LOGGER = logging.getLogger(__name__)

def add_task(data):
    """Add a new task to the list and return the created task."""
    task = task_creation_schema.load(data)
    LOGGER.debug("Task from request: %s", task)
    db.session.execute(db.insert(Task).values(
        task=task.task,
        due_date=task.due_date
    ))
    db.session.commit()

def list_tasks():
    """Return the list of all tasks."""
    tasks = db.session.execute(db.select(Task)).scalars()
    return task_schema.dump(tasks, many=True)
