import logging
from flask import Blueprint, request, jsonify
from services.task_service import add_task, list_tasks
from decorators import log_endpoint

LOGGER = logging.getLogger(__name__)
tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('', methods=['GET'])
@log_endpoint
def get_tasks():
    """Retrieve all tasks."""
    LOGGER.info("Fetching all tasks")
    tasks = list_tasks()
    return jsonify({"success": True, "message": tasks}), 200

@tasks_bp.route('', methods=['POST'])
@log_endpoint
def create_task():
    """Create a new task with a 'task' description and a 'due_by' timestamp."""
    data = request.get_json()
    LOGGER.info("Creating task with data: %s", data)
    add_task(data)
    return jsonify({"success": True, "message": "Task created successfully"}), 201
