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
        {'code': "Monday", 'label': "Понеділок"},
        {'code': "Tuesday", 'label': "Вівторок"},
        {'code': "Wednesday", 'label': "Середа"},
        {'code': "Thursday", 'label': "Четвер"},
        {'code': "Friday", 'label': "П'ятниця"},
        {'code': "Saturday", 'label': "Субота"},
        {'code': "Sunday", 'label': "Неділя"}
    ])

def downgrade():
    # Видалити таблицю при відкаті міграції
    op.drop_table('dictionary_schedule_day')