#!/usr/bin/python3
"""defines a class, City
and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """defines the City class (with sqlalchemy datatypes )
    which defines the City table (to be created)"""

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
