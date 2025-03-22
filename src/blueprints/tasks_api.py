from flask import Blueprint, request, jsonify
from services.task_service import add_task, list_tasks

tasks_api_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_api_bp.route('', methods=['GET'])
def get_tasks():
    """Retrieve all tasks."""
    tasks = list_tasks()
    return jsonify({"tasks": tasks})

@tasks_api_bp.route('', methods=['POST'])
def create_task():
    """Create a new task with a 'task' description and a 'due_by' timestamp."""
    data = request.get_json()
    # TODO - is there schema validator library?
    if not data or 'task' not in data or 'due_by' not in data:
        return jsonify({"success": False, "message": "Invalid data, must include 'task' and 'due_by' keys."}), 400
    
    # TODO - Validate the due_by timestamp format, this should be in the format DD-MM-YYYY

    new_task = add_task(data)
    return jsonify({"success": True, "message": "Task created successfully", "task": new_task}), 201

