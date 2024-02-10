import unittest
import sys
sys.path.append('../')
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_default_constructor(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertNotEqual(obj.id, '')
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_empty_kwargs(self):
        obj = BaseModel(**{})
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertNotEqual(obj.id, '')
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_missing_attributes_in_kwargs(self):
        obj = BaseModel(id='test_id', created_at=datetime.now().isoformat())
        self.assertEqual(obj.id, 'test_id')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_invalid_kwargs(self):
        with self.assertRaises(ValueError):
            obj = BaseModel(created_at='invalid_date_format')
if __name__ == '__main__':
    unittest.main()
