import unittest
import sys
sys.path.append('../')
import uuid
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
  def test_default_constructor(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertNotEqual(obj.id, '')
        self.assertEqual(obj.created_at, obj.updated_at)
        

if __name__ == '__main__':
    unittest.main()