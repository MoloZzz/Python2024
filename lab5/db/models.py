from sqlalchemy import Column, Integer, String, ForeignKey,UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Discipline(Base):
    __tablename__ = 'discipline'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    professor = Column(String)
    credits = Column(Integer)
    __table_args__ = (
        UniqueConstraint('name', 'professor'),
    )

class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    discipline_id = Column(Integer, ForeignKey('discipline.id'))
    discipline = relationship("Discipline")
    day_code = Column(String, ForeignKey('dictionary_schedule_day.code'))
    day = relationship("DictionaryScheduleDay")
    time = Column(String)
    __table_args__ = (
        UniqueConstraint('discipline_id', 'day_code', 'time'),
    )

class DictionaryScheduleDay(Base):
    __tablename__ = 'dictionary_schedule_day'

    code = Column(String, primary_key=True)
    label = Column(String)