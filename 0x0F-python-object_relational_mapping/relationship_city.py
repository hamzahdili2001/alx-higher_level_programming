#!/usr/bin/python3
"""Improve the files model_city.py"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, String, Integer, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Improve the files model_city.py"""

    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True,
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    def __init__(self, name):
        """Initialize City instance/object"""
        self.name = name
