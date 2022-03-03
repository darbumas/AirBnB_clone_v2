#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
=======
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
>>>>>>> 23930bb2b4653485181bdb5643d77ce988e6e53f


class User(BaseModel, Base):
    """This class defines a User object"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
<<<<<<< HEAD
    first_name = Column(String(128))
    last_name = Column(String(128))


=======
<<<<<<< HEAD
<<<<<<< HEAD
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Places', backref='user', cascade='all')
>>>>>>> 23930bb2b4653485181bdb5643d77ce988e6e53f
=======
=======
>>>>>>> parent of 9f2cbb7... confirm changes
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
>>>>>>> 168a0ba9cb1e28b9d47a30884a73d0e53bbb58a8
<<<<<<< HEAD
>>>>>>> parent of 9f2cbb7... confirm changes
=======
>>>>>>> parent of 9f2cbb7... confirm changes
