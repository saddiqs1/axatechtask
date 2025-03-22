

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from db import db
from . import tasks_table_name

class Task(db.Model):
    __tablename__ = tasks_table_name

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)

class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True