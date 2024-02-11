#!/usr/bin/python3
"""this module for test the class of the user and his methods."""

import unittest
from models import place

import unittest
from unittest.mock import patch
import sys


from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City


class TestCity(unittest.TestCase):
    """this the test of city class"""

    def test0_attributes(self):
        city_x = City()
        self.assertEqual(city_x.__class__.__name__, 'City')

    def test1_attributes(self):
        city_y = City('test', 5)
        self.assertTrue(isinstance(city_y.id, str))
        self.assertIsInstance(city_y.name, str)

    def test2_attributes(self):
        city_x = City()
        city_y = City('test', 5)
        self.assertTrue(isinstance(city_y.id, str))
        self.assertIsInstance(city_y.name, str)
        self.assertNotEqual(city_x, city_y)

    def test3_attributes(self):
        city_x = City()
        self.assertIn(city_x.created_at.isoformat(), city_x.to_dict().values())

    def test4_attributes(self):
        city_x = City()
        city_x.name = 'GIza'
        self.assertIn('name', city_x.to_dict().keys())

    def test5_attributes(self):
        city_x = City()
        city_x.name = 'GIza'
        self.assertIn('City', city_x.to_dict().values())

    def test6_attributes(self):
        city_x = City()
        city_x.name = 'GIza'
        self.assertIn('City', city_x.__str__())

    def test0_save(self):
        object = City()
        object.save()
        self.assertIsInstance(object.updated_at, datetime)

    def test1_save(self):
        object = City()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test2_save(self):
        object = City()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test0_storage(self):
        object = City()
        self.assertIn('City' + '.' + object.id, storage.all().keys())

    def test1_storage(self):
        object = City()
        my_key = 'City' + '.' + object.id
        self.assertIn('City' + '.' + object.id, storage.all().keys())
        self.assertIn('City', (storage.all())[my_key].to_dict().values())
