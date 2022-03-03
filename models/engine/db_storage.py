#!/usr/bin/python3

from multiprocessing import pool
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref





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
        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                        .format(DIAL, DRIVER, USER, PASS, HOST, DB), pool_pre_ping=True)
        env = os.getenv('HBNB_ENV', 'development')
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.session = self.Session()
        self.classes = Base.__subclasses__()

    def get(self, cls, id):
        """
        Returns an object based on the class name and id
        """
        return self.session.query(cls).filter_by(id=id).first()

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
