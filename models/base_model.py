#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from turtle import up
import uuid
from datetime import datetime
from sqlalchemy import declarative_base, Column, String, DateTime

Base = declarative_base()

class BaseModel(Base):
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        __tablename__ = self.__class__.__name__.lower()
        
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = value
                elif key == 'updated_at':
                    self.updated_at = value
                elif key == 'id':
                    self.id = value
                else:
                    setattr(self, key, value)

        # if not kwargs:
        #     from models import storage
        #     self.id = str(uuid.uuid4())
        #     self.created_at = datetime.now()
        #     self.updated_at = datetime.now()
        #     storage.new(self)
        # else:
        #     kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
        #                                              '%Y-%m-%dT%H:%M:%S.%f')
        #     kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
        #                                              '%Y-%m-%dT%H:%M:%S.%f')
        #     del kwargs['__class__']
        #     self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes an instance from storage"""
        from models import storage
        storage.delete(self)
