# In-memory list to store tasks.
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
    return tasks
