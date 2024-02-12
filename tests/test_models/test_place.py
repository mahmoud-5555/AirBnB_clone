#!/usr/bin/python3
"""this module used for test place class"""

import unittest
from unittest.mock import patch
import sys


from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place


class TestPlse(unittest.TestCase):
    """this the test of place class"""
    def test0_attributes(self):
        place_x = Place()
        self.assertEqual(place_x.__class__.__name__, 'Place')

    def test1_attributes(self):
        place_y = Place('test', 5)
        self.assertTrue(isinstance(place_y.id, str))
        self.assertIsInstance(place_y.name, str)

    def test2_attributes(self):
        place_x = Place()
        place_y = Place('test', 5)
        self.assertTrue(isinstance(place_y.id, str))
        self.assertIsInstance(place_y.name, str)
        self.assertNotEqual(place_x, place_y)

    def test3_attributes(self):
        place_x = Place()
        lov = place_x.to_dict().values()
        self.assertIn(place_x.created_at.isoformat(), lov)

    def test4_attributes(self):
        place_x = Place()
        place_x.name = 'GIza'
        self.assertIn('name', place_x.to_dict().keys())

    def test5_attributes(self):
        place_x = Place()
        place_x.name = 'GIza'
        self.assertIn('Place', place_x.to_dict().values())

    def test6_attributes(self):
        place_x = Place()
        place_x.name = 'GIza'
        self.assertIn('Place', place_x.__str__())

    def test0_save(self):
        object = Place()
        object.save()
        self.assertIsInstance(object.updated_at, datetime)

    def test1_save(self):
        object = Place()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test2_save(self):
        object = Place()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test0_storage(self):
        object = Place()
        self.assertIn('Place' + '.' + object.id, storage.all().keys())

    def test1_storage(self):
        object = Place()
        my_key = 'Place' + '.' + object.id
        self.assertIn('Place' + '.' + object.id, storage.all().keys())
        self.assertIn('Place', (storage.all())[my_key].to_dict().values())
