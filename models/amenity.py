#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity

class Amenity(BaseModel):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)