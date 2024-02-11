"""this module used for test State class"""

import unittest
from unittest.mock import patch
import sys


from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.state import State


class TestPlse(unittest.TestCase):
    """this the test of State class"""
    def test0_attributes(self):
        State_x = State()
        self.assertEqual(State_x.__class__.__name__, 'State')

    def test1_attributes(self):
        State_y = State('test', 5)
        self.assertTrue(isinstance(State_y.id, str))

    def test2_attributes(self):
        State_x = State()
        State_y = State('test', 5)
        self.assertTrue(isinstance(State_y.id, str))
        self.assertNotEqual(State_x, State_y)

    def test3_attributes(self):
        State_x = State()
        lov = State_x.to_dict().values()
        self.assertIn(State_x.created_at.isoformat(), lov)

    def test4_attributes(self):
        State_x = State()
        State_x.name = 'GIza'
        self.assertIn('name', State_x.to_dict().keys())

    def test5_attributes(self):
        State_x = State()
        State_x.name = 'GIza'
        self.assertIn('State', State_x.to_dict().values())

    def test6_attributes(self):
        State_x = State()
        State_x.name = 'GIza'
        self.assertIn('State', State_x.__str__())

    def test0_save(self):
        object = State()
        object.save()
        self.assertIsInstance(object.updated_at, datetime)

    def test1_save(self):
        object = State()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test2_save(self):
        object = State()
        object.save()
        self.assertNotEqual(object.created_at, object.updated_at)

    def test0_storage(self):
        object = State()
        self.assertIn('State' + '.' + object.id, storage.all().keys())

    def test1_storage(self):
        object = State()
        my_key = 'State' + '.' + object.id
        self.assertIn('State' + '.' + object.id, storage.all().keys())
        self.assertIn('State', (storage.all())[my_key].to_dict().values())
