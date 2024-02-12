#!/usr/bin/python3
"""this module used for test User class"""

import unittest
from unittest.mock import patch
import sys


from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class TestPlse(unittest.TestCase):
    """this the test of User class"""
    def test0_attributes(self):
        User_x = User()
        self.assertEqual(User_x.__class__.__name__, 'User')

    def test1_attributes(self):
        User_y = User('test', 5)
        self.assertTrue(isinstance(User_y.id, str))

    def test2_attributes(self):
        User_x = User()
        User_y = User('test', 5)
        self.assertTrue(isinstance(User_y.id, str))
        self.assertNotEqual(User_x, User_y)

    def test3_attributes(self):
        User_x = User()
        lov = User_x.to_dict().values()
        self.assertIn(User_x.created_at.isoformat(), lov)

    def test4_attributes(self):
        User_x = User()
        User_x.name = 'GIza'
        self.assertIn('name', User_x.to_dict().keys())

    def test5_attributes(self):
        User_x = User()
        User_x.name = 'GIza'
        self.assertIn('User', User_x.to_dict().values())

    def test6_attributes(self):
        User_x = User()
        User_x.name = 'GIza'
        self.assertIn('User', User_x.__str__())

    def test0_save(self):
        object = User()
        object.save()
        self.assertIsInstance(object.updated_at, datetime)

    def test1_save(self):
        object = User()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test2_save(self):
        object = User()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test0_storage(self):
        object = User()
        self.assertIn('User' + '.' + object.id, storage.all().keys())

    def test1_storage(self):
        object = User()
        my_key = 'User' + '.' + object.id
        self.assertIn('User' + '.' + object.id, storage.all().keys())
        self.assertIn('User', (storage.all())[my_key].to_dict().values())
