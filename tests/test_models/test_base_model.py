import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    def test___str__(self):
        object = BaseModel()
        object.id = "234-6787763-77"
        object.updated_at = datetime.datetime(2017, 11, 30, 21, 5, 54, 119427)
        object.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        str(object)
        expected_str = "[BaseModel] (234-6787763-77){'updated_at': datetime.datetime(11, 30, 21, 5, 54, 119427), 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}"

        self.assertEqual(str(object), expected_str)