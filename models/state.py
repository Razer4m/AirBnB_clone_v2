#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'  # Table name in the database

    name = Column(String(128), nullable=False)  # State name column

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete-orphan",
                              backref=backref("state", cascade="all"),
                              passive_deletes=True)
    else:
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
