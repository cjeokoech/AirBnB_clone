#!/usr/bin/python3
"""Define place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent place.

    Attributes:
    city_id(str): city id of the place
    user_id: user id of the place
    name(str): name of the plce
    description(str):description of the place
    number_rooms(int): number of rooms in place
    number_bathrooms(int): number of bathrooms in place
    max_guest(int): maximum guest in the place
    price_per_night(int): price per night in place
    latitude(float): latitude of the place
    longitude(float): longitude of the place
    amenity_id(list): amenity id of the place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
