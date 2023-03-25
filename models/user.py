#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', backref='user', cascade='delete')
        reviews = relationship('Review', backref='user', cascade='delete')
else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ""
        password = ""
        first_name = ""
