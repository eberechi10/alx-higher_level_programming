#!/usr/bin/python3

"""
Defines a State class that represents a table `states`.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """.
    Attributes:
        id (int): The primary key for the table.
        name (str): The name of the state.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        order_by="City.id",
        backref="state",
        cascade="all, delete, delete-orphan",
    )
