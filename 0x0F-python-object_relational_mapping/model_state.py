#!/usr/bin/python3
""" Creating orm abstraction with sql alchemy """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attribute:
        __table_name__ : name of the table
        id : state id
        name : names of the states

    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
