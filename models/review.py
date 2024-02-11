#!/usr/bin/python3
"""Define review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent review class.

    Attributes:
    place_id(str): place id of review
    user_id(str): user id of review
    text(str): text on review
    """
    plce_id = ""
    user_id = ""
    text = ""
