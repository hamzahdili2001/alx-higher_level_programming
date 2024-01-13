#!/usr/bin/python3
""" the class definition of a State and an
instance Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """the class definition of a State
    and an instance Base = declarative_base()"""

    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True,
    )
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """init"""
        self.name = name
