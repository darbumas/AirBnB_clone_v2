#!/usr/bin/python3
from multiprocessing import pool
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
import models
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class_list = [City, State, User, Place, Review, Amenity]

class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        """
        Initializes engine and session
        """
        DIAL='mysql'
        DRIVER = 'mysqldb'
        USER = os.environ.get('HBNB_MYSQL_USER')
        PASS = os.environ.get('HBNB_MYSQL_PWD')
        HOST = os.environ.get('HBNB_MYSQL_HOST')
        DB = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'.format(DIAL, DRIVER, USER, PASS, HOST, DB),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary of all objects
        """
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                obj.reload()
            return objs
        else:
            objs = {}
            for c in class_list:
                objs[c.__name__] = self.all(c)
            return objs

    def new(self, obj):
        """
        adds object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commits all changes of current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes obj from current database session if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        reloads the database session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))



    def close(self):
        """
        calls remove() on private sessionmaker object
        """
        self.__session.remove()


