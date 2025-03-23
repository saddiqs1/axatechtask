from datetime import datetime
from marshmallow import Schema, ValidationError, fields, post_load, validates

from models.task import Task


class TaskCreationSchema(Schema):
    task = fields.String(required=True)
    due_date = fields.DateTime(required=False, format="%d-%m-%Y %H:%M")

    @validates("due_date")
    def validates_due_date(self, value):
        if value < datetime.now():
            raise ValidationError("Datetime cannot be in the past.")
        
    @post_load
    def make_task(self, data, **kwargs):
        return Task(**data)