#!/usr/bin/python3
"""Define BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A base class that define commont attributes and methods of HBNB project
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel class.
        Args:
        *args: unused arguemt
        **kwargs: key word arguments containing values to arguments.
        """
        ift = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, ift)
                else:
                    self.__dict__[key] = value
            else:
                models.storage.new(self)
    def __str__(self):
        """
        Return string representation of BaseModel instance.
        Returns:
        str: string containing the calss
        name, id and attribute.
        """
        j = self.__class__.__name__
        return "[{}] ({}) {}".format(j, self.id, self.__dict__)
    def save(self):
        """
        Update the 'updated_at' attribute
        with current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()
    def  to_dict(self):
        """
        a dictionary representation.
        Returns:
        dict: a dictionary
        """
        o_dict = self.__dict__.copy()
        o_dict['__class__'] = self.__class__.__name__
        o_dict['created_at'] = self.created_at.isoformat()
        o_dict['updated_at'] = self.updated_at.isoformat()
        return o_dict
