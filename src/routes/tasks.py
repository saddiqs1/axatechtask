import logging
from flask import Blueprint, request, jsonify
from services.task_service import add_task, list_tasks

LOGGER = logging.getLogger(__name__)
tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('', methods=['GET'])
def get_tasks():
    """Retrieve all tasks."""
    tasks = list_tasks()
    return jsonify({"success": True, "message": tasks})

@tasks_bp.route('', methods=['POST'])
def create_task():
    """Create a new task with a 'task' description and a 'due_by' timestamp."""
    data = request.get_json()
    add_task(data)
    return jsonify({"success": True, "message": "Task created successfully"}), 201
