#!/usr/bin/python3
"""
this file will be response
of convert opject to json and
save it to file
"""
import json,os
from ..base_model import BaseModel

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
        self.__objects[ opj.__class__.__name__+'.'+ opj.id ] = opj

    def save(self):
        with open(self.__file_path,'w+', encoding='UTF-8') as json_file:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()

            json.dump(obj_dict, json_file, indent=2)
    

    def reload(self):
        with open(self.__file_path, 'r+', encoding='UTF-8') as json_file:
            if json_file.read():
                json_file.seek(0)  # Move the file pointer to the beginning
                obj_dict = json.load(json_file)
                for key,value in obj_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
                    
                #print(str(obj_dict))
