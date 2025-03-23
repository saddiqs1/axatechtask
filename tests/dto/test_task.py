from freezegun import freeze_time
import pytest
from marshmallow import ValidationError
from src.dto.task import TaskCreationSchema

mock_date = "2025-03-23 12:00:00"
valid_date = "27-03-2025 15:30"

@freeze_time(mock_date)
def test_due_date_in_past():
    schema = TaskCreationSchema()
    data = {"task": "Some task", "due_date": "21-03-2025 15:30"}
    with pytest.raises(ValidationError) as exc_info:
        schema.load(data)
    assert "Datetime cannot be in the past." in str(exc_info.value)

@freeze_time(mock_date)
def test_due_date_in_future():
    schema = TaskCreationSchema()
    data = {"task": "Some task", "due_date": valid_date}
    result = schema.load(data)
    assert result is not None
    assert result.task == data["task"]
    assert result.due_date.strftime("%d-%m-%Y %H:%M") == valid_date

@freeze_time(mock_date)
def test_due_date_is_none():
    schema = TaskCreationSchema()
    data = {"task": "Some task"}
    result = schema.load(data)
    assert result.due_date is None

@freeze_time(mock_date)
def test_task_is_none():
    schema = TaskCreationSchema()
    data = {"task": None, "due_date": valid_date}
    with pytest.raises(ValidationError) as exc_info:
        schema.load(data)
    errors = exc_info.value.messages
    assert "task" in errors

@freeze_time(mock_date)
def test_task_random_text():
    schema = TaskCreationSchema()
    data = {"task": "random text", "due_date": valid_date}
    result = schema.load(data)
    assert result is not None
    assert result.task == "random text"
    assert result.due_date.strftime("%d-%m-%Y %H:%M") == valid_date
