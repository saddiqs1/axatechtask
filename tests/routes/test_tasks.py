from datetime import datetime

def mock_list_tasks():
    return [{"task": "this is a task", "due_date": None}]

def mock_add_task(data):
    pass

def test_get_tasks(monkeypatch, flask_app):    
    monkeypatch.setattr("routes.tasks.list_tasks", mock_list_tasks)
    
    response = flask_app.get("/tasks")

    assert response.status_code == 200

    data = response.json
    assert data["success"] == True
    assert len(data["message"]) == 1
    assert data["message"][0]["task"] == "this is a task"
    assert data["message"][0]["due_date"] == None


def test_create_task(monkeypatch, flask_app):    
    monkeypatch.setattr("routes.tasks.add_task", mock_add_task)
    
    response = flask_app.post("/tasks", json={
        "task": "this is a task",
        "due_date": "27-03-2025 15:30"
    })

    assert response.status_code == 201

    data = response.json
    assert data["success"] == True
    assert data["message"] == "Task created successfully"