#!/usr/bin/python3
"""
Class definition of 'City'
"""
from model_state import State, Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
    connects to the table "cities" and sets up the columns id and name
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
