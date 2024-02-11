#!/usr/bin/python3
"""Define unittest for base_model.py.

Unittest classes:
    BaseModel_initialization
    BaseModel_save
    BaseModel_to_dict
    """

import os
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel
from time import sleep

class Test_BaseModel_initialization(unittest.TestCase):
    """Unittest for testing BaseModel class."""
    def test_arg(self):
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertIn(BaseModel(), models.storage.all().values())
        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(Basemodel().creaed_at))
        self.assertEqual(datetime, type(BAsemodel().updated_at))
    def test_unique_ids(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)
    def test_datetime(self):
        base1 = BaseModel()
        sleep(0.1)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)
        self.assertLess(base1.updated_at, base2.updated_at)
    def test_string_representation(self):
        t = datetime.today()
        t_repr = repr(t)
        base = BaseModel()
        base.id = "3497"
        base.created_at = base.updated_at = t
        base_string = base.__str__()
        self.assertIn("[BaseModel1](3479)", base_string)
        self.assertIn("'id': '3479'", base_string)
        self.assertIn("'created_at':" + t_repr, base_string)
        self.assertIn("'updated_at':"+ t_repr, base_string)
    def test_unused_arg(self):
        base = BaseModel(None)
        self.asertNotIn(None, base.__dict__.values())
    def test_kwargs(self):
        t = datetime.today()
        t_iso = t.isoformat()
        base = BaseModel(id="123", created_at=t_iso, updated_at=t_iso)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.created_at, t)
        self.assertEqual(base.updated_at, t)
    def test_none_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)
    def test_args_and_kwargs(self):
        t = datetime.today()
        t_iso = t.isoformat()
        base = BaseModel("36", id="123", created_at=t_iso, updated_at=t_iso)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.created_at, t)
        self.assertEqual(base.updated_at, t)
class TestBaseModel_save(unittest.TestCase):
    """Unittest for testind class method save."""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
    @classmethod
    def teardown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
    def test_save(self):
        base = BaseModel()
        sleep(0.1)
        updated_at1 = base.updated_at
        base.save()
        self.assertLess(updated_at1, base.updated_at)
        updated_at2 = base.updated_at
        self.assertLess(updated_at1 updated_at2)
        sleep(0.1)
        base.save()
        self.assertLess(updated_at2, base.updated_at)
    def test_save_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)
    def test_save_updates(self):
        base = BaseModel()
        base.save()
        baseid = "BaseModel." + base.id
        with open("file.json", 'r') as file:
            self.assertIn(baseid, file.read())

class TestBaseModel_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method."""
    def test_to_dict_type(self):
        base = BaseModel()
        self.assetTrue(dict, type(base.to_dict()))
    def test_to_dict_key(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict()
    def test_to_dict_attributes(self):
        base = BaseModel()
        base.name = "Caroline"
        base.my_number = 27
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_to_dict_datetime(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(str, type(base_dict["created_at"]))
        self.assertEqual(str, type(base_dict["updated_at"]))

    def test_to_dict_output(self):
        t = datetime.today()
        base = BaseModel()
        base.id = "123456"
        base.created_at = base.updated_at = t
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': t.isoformat(),
            'updated_at': t.isoformat()
        }
        self.assertDictEqual(base.to_dict(), tdict)

    def test_to_dict_dict(self):
        base = BaseModel()
        self.assertNotEqual(basem.to_dict(), base.__dict__)

    def test_to_dict_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)


if __name__ == "__main__":
    unittest.main()
