#!/usr/bin/python3
"""Define user class that inherit from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent user.

    Attributes:
    Email(str): user email
    password(str): user password
    first_name(str): user first name
    last_name(str): user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
