#!/usr/bin/python3
import uuid,datetime

"""this the base module"""
class BaseModel:
    """
    this will be the base class for all other models
    in our application. It provides common functionalities
    to all classes.
    """
    def __init__(self):
        """
        this is the constructor of the base class that not take
        any argumants and no return value "NULL"
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
    
    def __str__(self):
        """
        this is the constructor of the base class that not take
        any argumants and return object in dictionary representation
        """
        obj_dict = (self.__dict__).copy()
        
    
        return '[{}] (<{}>) <{}>'.\
        format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """
        this function  it take
        a new value of updated_at as argumant and return nothing
        """
        self.updated_at = datetime.datetime.now()

    
    
    def to_dict(self):
        """
        this function  it has no argumants and  returns 
        a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = {
            '__class__': self.__class__.__name__,
        }
        obj_dict.update(self.__dict__)

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


