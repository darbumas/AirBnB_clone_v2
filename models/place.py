#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, \
    Float, Table
from sqlalchemy.orm import relationship
import os

class Place(BaseModel, Base):
    """ Place class handles all application places """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, default="")
    number_rooms = Column(Integer, nullable=True, default=0)
    number_bathrooms = Column(Integer, nullable=True, default=0)
    max_guest = Column(Integer, nullable=True, default=0)
    price_by_night = Column(Integer, nullable=True, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        @property
        def reviews(self):
            """ Return all reviews for a place """
            return self.reviews

    # else:
    #     city_id = ""
    #     user_id = ""
    #     name = ""
    #     description = ""
    #     number_rooms = 0
    #     number_bathrooms = 0
    #     max_guest = 0
    #     price_by_night = 0
    #     latitude = 0.0
    #     longitude = 0.0
    #     reviews = []


#     @reviews.setter
#     def reviews(self, value):
#         """ setter for reviews """
#         if type(value) != list:
#             self.reviews.append(value)
#         else:
#             self.reviews = value

    # @reviews.deleter
    # def reviews(self):
    #     """ deleter for reviews """
    #     del self.reviews

    # def __init__(self, *args, **kwargs):
    #     """ initializes place """
    #     super().__init__(*args, **kwargs)
    #     if kwargs:
    #         for key, value in kwargs.items():
    #             if key == "city_id" or key == "user_id":
    #                 setattr(self, key, value)
    #             elif key == "name":
    #                 self.name = value
    #             elif key == "description":
    #                 self.description = value
    #             elif key == "number_rooms":
    #                 self.number_rooms = value
    #             elif key == "number_bathrooms":
    #                 self.number_bathrooms = value
    #             elif key == "max_guest":
    #                 self.max_guest = value
    #             elif key == "price_by_night":
    #                 self.price_by_night = value
    #             elif key == "latitude":
    #                 self.latitude = value
    #             elif key == "longitude":
    #                 self.longitude = value
    #             elif key == "reviews":
    #                 self.reviews = value
    #             else:
    #                 pass
    #     else:
    #         pass

    # def __str__(self):
    #     """ returns string representation of place """
    #     return "[Place] ({}) {}".format(self.id, self.__dict__)

    # def to_dict(self):
    #     """ returns dictionary representation of place """
    #     new_dict = super().to_dict()
    #     new_dict['reviews'] = []
    #     for review in self.reviews:
    #         new_dict['reviews'].append(review.to_dict())
    #     return new_dict

    # def to_json(self):
    #     """ returns json representation of place """
    #     new_dict = self.to_dict()
    #     return new_dict

=======
from sqlalchemy import Column, String, Integer, Float, ForeignKey

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
>>>>>>> 23930bb2b4653485181bdb5643d77ce988e6e53f
