import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    def test__str__(self):
        # Create an instance of BaseModel
        obj = BaseModel()
        obj.id = "234-6787763-77"
        obj.updated_at = (2017, 11, 30, 21, 5, 54, 119427)
        obj.created_at = (2017, 9, 28, 21, 5, 54, 119427)

        # Call the __str__() method
        actual_str = str(obj)

        # Define the expected string representation
        expected_str = "[BaseModel] (234-6787763-77){'updated_at': (2017, 11, 30, 21, 5, 54, 119427), 'created_at': (2017, 9, 28, 21, 5, 54, 119427)}"

        # Compare the actual and expected string representations
        self.assertEqual(actual_str, expected_str)

if __name__ == '__main__':
    unittest.main()