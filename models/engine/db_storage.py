#!/usr/bin/python3

from multiprocessing import pool
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref


HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')



class DBStorage:
        def __init__(__engine, __session):
            """
            Initializes DBStorage class
            """
            __engine = create_engine
            ('mysql+mysqldb://{}:{}@{}/{}'.format
                                                (HBNB_MYSQL_USER, HBNB_MYSQL_PWD, 
                                                 HBNB_MYSQL_HOST, HBNB_MYSQL_DB, pool_pre_ping=True))
            __session = scoped_session
            (sessionmaker(autocommit=False, expire_on_commit=False,
                                                    autoflush=False, bind=__engine))
    

        def all(self, cls=None):
            """
            Returns all objects depending on the class name
            """
            if cls is not None:
                obj = self.session.query(cls).all()
            else:
                obj = self.session.query(self.classes).all()
            return obj

        def new(self, obj):
            """
            Adds new object to storage
            """
            self.session.add(obj)

        def save(self):
            """
            Commits all changes
            """
            self.session.commit()

        def delete(self, obj=None):
            """
            Deletes object from storage
            """
            self.session.delete(obj)

        def reload(self):
            """
            Reloads all objects from storage
            """
            self.session = self.Session()

        def close(self):
            """
            Closes the session
            """
            self.session.close()

