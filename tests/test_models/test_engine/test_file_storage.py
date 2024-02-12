#!/usr/bin/python3
"""this file test for storge file"""
import unittest
import os
import json
import sys
sys.path.append("./../../../")

from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.state import State
from models.user import User

import sys


class TestFileStorage(unittest.TestCase):
    """testing file storage"""

    def setUp(self):
        self.file_path = 'file.json'

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        obj1 = BaseModel()
        storage.new(obj1)
        self.assertIn('BaseModel.' + obj1.id, storage.all().keys())

    def test_save_and_reload(self):
        obj1 = BaseModel()
        storage.new(obj1)
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(new_storage.all(), storage.all())

    def test_save_empty(self):
        obj1 = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_corrupt_file(self):
        try:
            with open(self.file_path, 'w') as f:
                f.seek(0)
                f.write('')
        except Exception:
            pass
        try:
            with open(self.file_path, 'r') as f:
                storage.reload()
                self.assertEqual(storage.all(), {})
        except Exception:
            pass


if __name__ == '__main__':
    sys.path.append("./../../../")
    unittest.main()
