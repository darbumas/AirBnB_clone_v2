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
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Places', backref='user', cascade='all')
>>>>>>> 23930bb2b4653485181bdb5643d77ce988e6e53f
