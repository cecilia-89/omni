#!/usr/bin/python3
"""Module: movie, contains the model movie"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

movie_actors = Table(
	"movie_actors",
	Base.metadata,
	Column('movie_id', ForeignKey('movie.id')),
	Column('actor_id', ForeignKey('actor.id')),
)

class Movie(BaseModel, Base):
	__tablename__ = 'movie'
	url = Column(String(2064), nullable=False)
	title = Column(String(64), nullable=False)
	series = Column(Boolean, default=False, nullable=True)
	rated_18 = Column(Boolean, default=False, nullable=True)
	genre_id = Column(String(64), ForeignKey('genre.id'), nullable=False)
	thumbnail = Column(String(2064), nullable=True)
	description = Column(String(6000), nullable=False)
	actors = relationship('Actor', secondary=movie_actors)