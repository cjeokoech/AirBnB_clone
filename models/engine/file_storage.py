#!/usr/bin/python3
"""Define the fileStorage class."""
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel

class FileStorage:
    """Represent storage engine.
    Attributes:
    __file_path:  string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """" Return the dictionary __object."""
        return FileStorage.__objects
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    def save(self):
        """Seriliaze __objects to JON file."""
        s = FileStorage.__objects
        s_obj = {obj:s[obj].to_dict() for obj in s.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(s_obj, file)
    def reload(self):
        """Deserialize the json file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                l = json.load(file)
                for o in l.values():
                    c_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(c_name)(**o))
        except FileNotFoundError:
            return
