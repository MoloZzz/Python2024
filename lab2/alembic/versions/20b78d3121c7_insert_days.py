"""insert_days

Revision ID: 20b78d3121c7
Revises: 
Create Date: 2024-05-15 12:00:00

"""
from alembic import op
import sqlalchemy as sa

# Змініть цю стрічку на відповідний імпорт моделі, якщо потрібно
from db.models import DictionaryScheduleDay

# Задайте унікальний ідентифікатор ревізії
revision = '20b78d3121c7'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Додати дані
    op.bulk_insert(DictionaryScheduleDay.__table__, [
        {'code': 1, 'label': 'Monday'},
        {'code': 2, 'label': 'Tuesday'},
        {'code': 3, 'label': 'Wednesday'},
        {'code': 4, 'label': 'Thursday'},
        {'code': 5, 'label': 'Friday'},
        {'code': 6, 'label': 'Saturday'},
        {'code': 7, 'label': 'Sunday'}
    ])

def downgrade():
    # Видалити таблицю при відкаті міграції
    op.drop_table('dictionary_schedule_day')