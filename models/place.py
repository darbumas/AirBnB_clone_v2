#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, \
    Float, Table
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ Place class handles all application places """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="all")

    @property
    def reviews(self):
        """Getter returns Review instances with 'place_id'"""
        my_list = []
        for place in storage.all(Review).values():
            if place.id == self.place_id:
                my_list.append(place)
        return my_list
