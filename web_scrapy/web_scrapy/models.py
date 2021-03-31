from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class QuoteDB(DeclarativeBase):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True)
    Title = Column('Title', Text())
    Price = Column('Price', Float())
    E_comerce = Column('E_comerce', String(100))
    Rating = Column('Rating', Float())
    Num_Validation = Column('Num_Validation', Integer())
    Link_Web = Column('Link_Web', Text())

    
    