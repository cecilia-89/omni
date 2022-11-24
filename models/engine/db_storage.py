#!/usr/bin/python3
"""Module: database storage"""
from models.base_model import Base
from models.actor import Actor
from models.genre import Genre
from models.movie import Movie
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

classes = [Actor, Genre, Movie]

class DBStorage:
    """database storage of omni"""

    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine(
                               "mysql+mysqldb://omni_user:omni_pwd@localhost/omni",
                                echo=True
                              )

    def reload(self):
        """creates tables in the database and sessions
        for interacting with the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        new_session = scoped_session(Session)
        self.__session = new_session

    def all(self, cls=None):
        """returns objects with the same class"""

        for clss in classes:
            if cls is clss:
                objects = self.__session.query(clss).all()

        return objects

    def get(self, cls, id):
        objs = self.all(cls)
        for obj in objs:
            if obj.id == id:
                return obj

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
