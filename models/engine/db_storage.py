#!/usr/bin/python3
""" DBStorage Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """ Database Storage class """

    __engine = None  # Private class attribute: set to None
    __session = None  # Private class attribute: set to None

    def __init__(self):
        """ Initialize DBStorage """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects depending on the class name """
        classes = [User, State, City, Amenity, Place, Review]
        objects_dict = {}

        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for cls in classes:
                objects.extend(self.__session.query(cls).all())

        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects_dict[key] = obj

        return objects_dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and create a session """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
