#!/usr/bin/python3
"""db_storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session

classes = ["State", "City", "User", "Place", "Review"]


class DBStorage:
    """class  dbstorage"""
    __engine = None
    __session = None

    def __init__(self):
        """ __init__(self) """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ all"""
        dect = {}
        if cls is not None:
            for inst in self.__session.query(cls).all():
                key = inst.__class__.__name__ + '.' + inst.id
                dect[key] = inst

        else:
            for clas in classes:
                clas = eval(clas)
                for inst in self.__session.query(clas).all():
                    key = inst.__class__.__name__ + '.' + inst.id
                    dect[key] = inst
        return dect

    def save(self):
        """ commit  """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete  """
        if obj:
            self.__session.delete(obj)

    def new(self, obj):
        """ add """
        self.__session.add(obj)

    def reload(self):
        """create reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session."""
        self.__session.close()
