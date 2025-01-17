#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import base_model
from models.base_model import Base, BaseModel
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey(
            'states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        name = ''
        state_id = ''
