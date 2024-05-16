from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

def connectDatabase():
    engine = create_engine('postgresql://postgres:5454@localhost:5432/python2_schedule', client_encoding='utf8')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()