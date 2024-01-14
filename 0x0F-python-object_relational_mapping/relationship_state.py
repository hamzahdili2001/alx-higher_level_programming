#!/usr/bin/python3
"""Improve the files model_state.py"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, String, Integer
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """Improve the files model_city.py"""

    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True,
    )
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade="all, delete, delete-orphan"
    )

    def __init__(self, name):
        """Initialize a State"""
        self.name = name
