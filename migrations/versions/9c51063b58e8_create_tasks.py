"""'create-tasks'

Revision ID: 9c51063b58e8
Revises: 
Create Date: 2025-03-22 03:26:29.553897

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
from src.models import tasks_table_name

revision: str = '9c51063b58e8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        tasks_table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("task", sa.Text, nullable=False),
        sa.Column("due_date", sa.DateTime, nullable=True),
    )

    tasks_table = sa.table(
        tasks_table_name,
        sa.column('id', sa.Integer),
        sa.column('task', sa.Text),
        sa.column('due_date', sa.DateTime)
    )

    op.bulk_insert(
        tasks_table,
        [
            {'id': 1, 'task': 'Create a presentation on chairs for Mr. Austin', 'due_date': datetime(2025, 1, 15, 10, 30)},
            {'id': 2, 'task': 'Have an april fools joke ready', 'due_date': datetime(2025, 4, 1)},
            {'id': 3, 'task': 'Dentist appointment', 'due_date': datetime(2025, 6, 23, 16, 15)},
            {'id': 4, 'task': 'Figure out how to make apple crumble', 'due_date': None},
        ]
    )

    op.get_bind().execute(text(
        """
            SELECT setval('tasks_id_seq', (SELECT MAX(id) FROM tasks));
			ALTER TABLE tasks ALTER COLUMN id SET DEFAULT nextval('tasks_id_seq'::regclass);
        """
        )
    )


def downgrade() -> None:
    op.drop_table(tasks_table_name)
