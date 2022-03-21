#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', backref='states',
            cascade='all, delete-orphan')
    else:
        name = ""
        cities = []

    @property
    def cities(self):
        """Returns a list of City instances"""
        my_list = []
        for city in models.storage.all(City).values():
            if self.id == city.state_id:
                my_list.append(city)
        return my_list
