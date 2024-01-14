#!/usr/bin/python3
"""Improve the files model_city.py"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """Improve the files model_city.py"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer, ForeignKey("states.id", ondelete="CASCADE"), nullable=False
    )
