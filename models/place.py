#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, MetaData
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

metadata = MetaData()
place_amenity = Table(
    'place_amenity',
    metadata,
    Column('place_id', String(60),
           ForeignKey('amenity_id'),
           primary_key=True, nullable=False),

    Column('amenity_id', String(60),
           ForeignKey('place_id'),
           nullable=False, primary_key=True))


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
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """Getter returns Review instances with 'place_id'"""
        my_list = []
        for place in storage.all(Review).values():
            if place.id == self.place_id:
                my_list.append(place)
        return my_list

    @property
    def amenities(self):
        """Getter for amenities_id"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, val):
        """Setter for amenities"""
        amenity_ids.append(val)
