#!/usr/bin/python3
"""this the test cacrss of base_model"""
import unittest
from unittest.mock import patch
import sys
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestBaseModel_the_constructor(unittest.TestCase):
    """this class to tests the Base module constructor"""

    def test1_default_constructor(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test2_default_constructor(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test3_default_constructor(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test4_default_constructor(self):
        obj = BaseModel()
        obj.id = '1212'
        self.assertEqual('1212', obj.id)

    def test5_default_constructor(self):
        obj = BaseModel()
        obj.my_number = 90
        self.assertEqual(obj.my_number, 90)

    def test6_default_constructor(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1, obj2)

    def test7_default_constructor(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test0_empty_kwargs(self):
        obj = BaseModel(**{})
        self.assertIsInstance(obj.id, str)

    def test1_empty_kwargs(self):
        obj = BaseModel(**{})
        self.assertNotEqual(obj.id, '')

    def test2_empty_kwargs(self):
        obj = BaseModel(**{})
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test3_empty_kwargs(self):
        obj = BaseModel(**{})
        self.assertEqual(obj.created_at, obj.updated_at)

    def test4_empty_kwargs(self):
        obj = BaseModel(**{})
        obj.my_number = 90
        self.assertEqual(obj.my_number, 90)

    def test5_empty_kwargs(self):
        obj = BaseModel(**{})
        obj.id = '1212'
        self.assertEqual('1212', obj.id)

    def test0_missing_attributes_in_kwargs(self):
        the_time = datetime.now().isoformat()
        obj = BaseModel(id='test_id', created_at=the_time)
        self.assertEqual(obj.id, 'test_id')

    def test1_missing_attributes_in_kwargs(self):
        the_time = datetime.now().isoformat()
        obj = BaseModel(id='test_id', created_at=the_time)

    def test2_missing_attributes_in_kwargs(self):
        the_time = datetime.now().isoformat()
        obj = BaseModel(id='test_id', created_at=the_time)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test3_missing_attributes_in_kwargs(self):
        the_time = datetime.now().isoformat()
        obj = BaseModel(id='test_id', created_at=the_time)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test4_missing_attributes_in_kwargs(self):
        the_time = datetime.now().isoformat()
        obj = BaseModel(id='test_id', created_at=the_time)
        obj.id = '1212'
        self.assertEqual('1212', obj.id)

    def test5_missing_attributes_in_kwargs(self):
        the_time = datetime.now().isoformat()
        obj = BaseModel(id='test_id', created_at=the_time)
        obj.my_number = 90
        self.assertEqual(obj.my_number, 90)

    def test6_missing_attributes_in_kwargs(self):
        the_time = datetime.now().isoformat()
        obj = BaseModel(created_at=the_time)
        self.assertNotEqual(None, obj.id)

    def test7_missing_attributes_in_kwargs(self):
        the_time = datetime.now().isoformat()
        obj = BaseModel(created_at=the_time)
        self.assertNotEqual('', obj.id)

    def test8_missing_attributes_in_kwargs(self):
        obj = BaseModel(my_number=20)
        self.assertNotEqual(None, obj.id)
        self.assertAlmostEqual(obj.my_number, 20)

    def test9_missing_attributes_in_kwargs(self):
        obj = BaseModel(my_number=20)
        self.assertNotEqual(obj.created_at, None)

    def test10_missing_attributes_in_kwargs(self):
        obj = BaseModel(my_number=20)
        self.assertNotEqual(obj.id, None)

    def test_invalid_kwargs(self):
        with self.assertRaises(ValueError):
            obj = BaseModel(created_at='invalid_date_format')


class TestBaseModel_to_dict_method(unittest.TestCase):
    """Unit tests for to_dict method of BaseModel"""
    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel(name='mahmoud', my_number=22, id='test_id')
        self.base_model_dict = {
            'id': self.b1.id,
            'created_at': self.b1.created_at.isoformat(),
            'updated_at': self.b1.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }

    def test0_to_dict(self):
        self.assertEqual(self.b1.to_dict(), self.base_model_dict)

    def test1_to_dict(self):
        self.assertIsInstance(self.b1.to_dict()['created_at'], str)

    def test2_to_dict(self):
        self.assertIsInstance(self.b1.to_dict()['updated_at'], str)

    def test3_to_dict(self):
        self.assertEqual(self.b1.to_dict()['__class__'], 'BaseModel')

    def test4_to_dict(self):
        self.assertEqual(self.b2.to_dict()['id'], 'test_id')

    def test5_to_dict(self):
        self.assertEqual(self.b2.to_dict()['my_number'], 22)

    def test6_to_dict(self):
        self.assertEqual(self.b2.to_dict()['name'], 'mahmoud')

    def test7_to_dict(self):
        self.assertIsInstance(self.b1.to_dict()['id'], str)

    def test8_to_dict(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.to_dict, obj2.to_dict)


class TestBaseModelStrMethod(unittest.TestCase):
    """Unit tests for __str__ method of BaseModel"""
    def setUp(self):
        self.base_model = BaseModel()
        self.base_model2 = BaseModel(**{})
        self.base_model3 = BaseModel(id='test', my_number=22)

    def test0_str(self):
        expected_str = "[BaseModel] ({}) {}".\
            format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test1_str(self):
        expected_str = "[BaseModel] ({}) {}".\
            format(self.base_model2.id, self.base_model2.__dict__)
        self.assertEqual(str(self.base_model2), expected_str)

    def test2_str(self):
        expected_str = "[BaseModel] ({}) {}".\
            format(self.base_model3.id, self.base_model3.__dict__)
        self.assertEqual(str(self.base_model3), expected_str)

    def test3_str(self):
        self.assertNotEqual(self.base_model2.__str__, self.base_model.__str__)

    def test3_str(self):
        self.assertNotEqual(self.base_model2.__str__, self.base_model3.__str__)

    def test4_str(self):
        self.assertIsInstance(self.base_model2.__str__(), str)


class TestBaseModelSaveMethod(unittest.TestCase):
    """Unit tests for save method of BaseModel"""

    def test0_save(self):
        base_model = BaseModel()
        base_model.save()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test1_save(self):
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(base_model.created_at, base_model.updated_at)

    def test2_save(self):
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(base_model.created_at, base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
