#!/usr/bin/python3
"""Module: database storage"""
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
import models
import uuid

Base = declarative_base()

class BaseModel:
    """base class upon which other class will be derived"""

    id = Column(String(60), primary_key=True)
    added_at = Column(DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """initializes an instance"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        self.id = uuid.uuid4()
        self.added_at = datetime.now()

    def save(self):
        """adds and saves instance to the database session"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """converts class instance to a dictionary"""
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['added_at'] = dict['added_at'].isoformat()

        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]

        return dict
