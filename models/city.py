#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ City class, contains state ID and name """
    __tablename__ = 'cities'  # Table name

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)  # Column: state_id (foreign key to states.id)
    name = Column(String(128), nullable=False)  # Column: name

    places = relationship("Place", back_populates="city", cascade="all, delete-orphan")  # Relationship with Place class
