#!/usr/bin/python3
"""this module used for test review class"""

import unittest
from unittest.mock import patch
import sys


from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.review import Review


class TestPlse(unittest.TestCase):
    """this the test of review class"""
    def test0_attributes(self):
        Review_x = Review()
        self.assertEqual(Review_x.__class__.__name__, 'Review')

    def test1_attributes(self):
        Review_y = Review('test', 5)
        self.assertTrue(isinstance(Review_y.id, str))

    def test2_attributes(self):
        Review_x = Review()
        Review_y = Review('test', 5)
        self.assertTrue(isinstance(Review_y.id, str))
        self.assertNotEqual(Review_x, Review_y)

    def test3_attributes(self):
        Review_x = Review()
        lov = Review_x.to_dict().values()
        self.assertIn(Review_x.created_at.isoformat(), lov)

    def test4_attributes(self):
        Review_x = Review()
        Review_x.name = 'GIza'
        self.assertIn('name', Review_x.to_dict().keys())

    def test5_attributes(self):
        Review_x = Review()
        Review_x.name = 'GIza'
        self.assertIn('Review', Review_x.to_dict().values())

    def test6_attributes(self):
        Review_x = Review()
        Review_x.name = 'GIza'
        self.assertIn('Review', Review_x.__str__())

    def test0_save(self):
        object = Review()
        object.save()
        self.assertIsInstance(object.updated_at, datetime)

    def test1_save(self):
        object = Review()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test2_save(self):
        object = Review()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test0_storage(self):
        object = Review()
        self.assertIn('Review' + '.' + object.id, storage.all().keys())

    def test1_storage(self):
        object = Review()
        my_key = 'Review' + '.' + object.id
        self.assertIn('Review' + '.' + object.id, storage.all().keys())
        self.assertIn('Review', (storage.all())[my_key].to_dict().values())
