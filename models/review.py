#!/usr/bin/python3
""" Review Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class """
    __tablename__ = 'reviews'  # Table name

    text = Column(String(1024), nullable=False)  # Column: text
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)  # Column: place_id (foreign key to places.id)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)  # Column: user_id (foreign key to users.id)

    user = relationship("User", back_populates="reviews")  # Relationship with User class
    place = relationship("Place", back_populates="reviews", cascade="all, delete-orphan")  # Relationship with Place class
