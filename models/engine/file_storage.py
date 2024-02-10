#!/usr/bin/python3
"""
this file will be response
of convert opject to json and
save it to file
"""
import json
import os


from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class FileStorage:
    """
    the class <FileStorage>
    class that response of  save object to a
    .json file.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, opj):
        """: sets in <__objects> the <obj> with key <obj class name>.id"""
        self.__objects[opj.__class__.__name__ + '.' + opj.id] = opj

    def save(self):
        """function that response to save the data in json file"""
        with open(self.__file_path, 'w+') as json_file:
            try:
                obj_dict = {}
                for key, value in self.__objects.items():
                    obj_dict[key] = value.to_dict()

                json.dump(obj_dict, json_file)
            except Exception:
                pass

    def reload(self):
        """reload objects from file"""
        with open(self.__file_path, 'w+') as json_file:
            try:
                if json_file.read():
                    json_file.seek(0)
                    obj_dict = json.load(json_file)
                    for key, value in obj_dict.items():
                        self.__objects[key] = eval(value['__class__'])(**value)
            except Exception:
                pass
