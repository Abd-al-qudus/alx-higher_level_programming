#!/usr/bin/python3

"""This script contains the definition of state object
    which inherits from the sql alchemy base class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class is the base class
        ___tablename__ : stores the name of the class
        id: state id
        name: state name"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
