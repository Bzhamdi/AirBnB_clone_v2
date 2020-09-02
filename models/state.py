#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """getter to list all cities"""
            from models import storage
            cities = models.storage.all(City).values()
            listofcities = []
            for city in cities:
                if city.state_id == self.id:
                    listofcities.append(city)

            return listofcities
