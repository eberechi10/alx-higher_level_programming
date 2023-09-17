#!/usr/bin/python3

"""
A module that defines a State class that reps a table `states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    a state in a database table.

    Attributes:
        id (int): The primary key for the table.
        name (str): The name of the state.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
