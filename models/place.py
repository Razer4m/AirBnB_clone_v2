#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ Place class """
    __tablename__ = 'places'  # Table name

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)  # Column: city_id (foreign key to cities.id)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)  # Column: user_id (foreign key to users.id)
    name = Column(String(128), nullable=False)  # Column: name
    description = Column(String(1024), nullable=True)  # Column: description
    number_rooms = Column(Integer, nullable=False, default=0)  # Column: number_rooms
    number_bathrooms = Column(Integer, nullable=False, default=0)  # Column: number_bathrooms
    max_guest = Column(Integer, nullable=False, default=0)  # Column: max_guest
    price_by_night = Column(Integer, nullable=False, default=0)  # Column: price_by_night
    latitude = Column(Float, nullable=True)  # Column: latitude
    longitude = Column(Float, nullable=True)  # Column: longitude

    user = relationship("User", back_populates="places")  # Relationship with User class
    city = relationship("City", back_populates="places")  # Relationship with City class

    reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")  # Relationship with Review class
