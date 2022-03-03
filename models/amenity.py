#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
# from models.place import place_amenity
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class Amenity(BaseModel, Base):
    """ Amenity class to store Amenity information """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

