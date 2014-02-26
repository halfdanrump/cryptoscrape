from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from settings import DATABASE

Base = declarative_base()

def connect():
	engine = create_engine(URL(**DATABASE))
	return engine

def create_tables(engine):
	Base.metadata.create_all(engine)

class NewsItem(Base):
	__tablename__ = 'newsitems'

	id = Column(Integer, primary_key = True)
	title = Column(String)
	link = Column(String)
	description = Column(String)
	summary = Column(String)
	rank = Column(Float)

