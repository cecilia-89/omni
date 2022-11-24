#!/usr/bin/python3
"""Module: actor, contains the model actor"""
from .base_model import Base, BaseModel
from sqlalchemy import Column, String

class Actor(BaseModel, Base):
	__tablename__ = 'actor'
	last_name = Column(String(32), nullable=False)
	first_name = Column(String(32), nullable=False)
