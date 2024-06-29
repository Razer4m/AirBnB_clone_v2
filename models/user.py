#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'  # Table name

    email = Column(String(128), nullable=False)  # Column: email
    password = Column(String(128), nullable=False)  # Column: password
    first_name = Column(String(128), nullable=True)  # Column: first_name
    last_name = Column(String(128), nullable=True)  # Column: last_name

    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")  # Relationship with Review class
