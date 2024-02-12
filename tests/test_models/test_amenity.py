#!/usr/bin/python3
"""this module used for test Amenity class"""
import sys
sys.path.append("./../../")

import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity


class TestPlse(unittest.TestCase):
    """this the test of Amenity class"""
    def test0_attributes(self):
        Amenity_x = Amenity()
        self.assertEqual(Amenity_x.__class__.__name__, 'Amenity')

    def test1_attributes(self):
        Amenity_y = Amenity('test', 5)
        self.assertTrue(isinstance(Amenity_y.id, str))

    def test2_attributes(self):
        Amenity_x = Amenity()
        Amenity_y = Amenity('test', 5)
        self.assertTrue(isinstance(Amenity_y.id, str))
        self.assertNotEqual(Amenity_x, Amenity_y)

    def test3_attributes(self):
        Amenity_x = Amenity()
        lov = Amenity_x.to_dict().values()
        self.assertIn(Amenity_x.created_at.isoformat(), lov)

    def test4_attributes(self):
        Amenity_x = Amenity()
        Amenity_x.name = 'GIza'
        self.assertIn('name', Amenity_x.to_dict().keys())

    def test5_attributes(self):
        Amenity_x = Amenity()
        Amenity_x.name = 'GIza'
        self.assertIn('Amenity', Amenity_x.to_dict().values())

    def test6_attributes(self):
        Amenity_x = Amenity()
        Amenity_x.name = 'GIza'
        self.assertIn('Amenity', Amenity_x.__str__())

    def test0_save(self):
        object = Amenity()
        object.save()
        self.assertIsInstance(object.updated_at, datetime)

    def test1_save(self):
        object = Amenity()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test2_save(self):
        object = Amenity()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test0_storage(self):
        object = Amenity()
        self.assertIn('Amenity' + '.' + object.id, storage.all().keys())

    def test1_storage(self):
        object = Amenity()
        my_key = 'Amenity' + '.' + object.id
        self.assertIn('Amenity' + '.' + object.id, storage.all().keys())
        self.assertIn('Amenity', (storage.all())[my_key].to_dict().values())
