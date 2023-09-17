#!/usr/bin/python3

"""
a module that define City class representing table `cities`
in the database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):

    """
     a module to initialize Cities.

    Attributes:
        id (int): primary key.
        name (str): city.
    """

    __tablename__ = 'cities'

    id: int = Column(Integer, primary_key=True)
    name: int = Column(String(128), nullable=False)
    state_id: int = Column(Integer, ForeignKey('states.id'))

    state = relationship('State', backref='cities')
