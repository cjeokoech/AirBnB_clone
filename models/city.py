#!/usr/bin/python3
"""Define city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent city.

    Attributes:
    name(str): name of the city
    state_id(str0: state id of the city
    """
    state_id = ""
    name = ""
