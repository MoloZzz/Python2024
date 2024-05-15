from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('postgresql://postgres:5454@localhost:5432/python2_schedule', client_encoding='utf8')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()