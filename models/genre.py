#!/usr/bin/python3
"""Module: genre, contains the model genre"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Genre(BaseModel, Base):
	__tablename__ = 'genre'
	title = Column(String(32), nullable=False)
	movie = relationship('Movie')
