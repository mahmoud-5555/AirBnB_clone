#!/usr/bin/python3
"""this the base module"""
import uuid,datetime
import models
class BaseModel:
    """
    this will be the base class for all other models
    in our application. It provides common functionalities
    to all classes.
    """ 

    def __init__(self, *args, **kwargs):
        self.id = ''
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        """
        construct the inctance from dictionary or from individual arguments
        kwargs: mast be the an attribute in the calss
        no return value 

        """
        """
        this method has many test ceass:
        first is the defulte constructor will work well
        what will happen if the <kwargs> is empty
        what will happen if the <kwargs> without <id> or <created_at>?
        what if the data wrteen wrong ? This will raise a ValueError
    
        >> idon't know how i will deal with it if the <updated_at> not found
        but in this case maybe we can create opject withot last update
        but the problem when we tring to re converted to josn >> the value of 
        the value of  <updated_at> will be None
        """
        """<isinstance_keys> list to save the attributes that asigned """
        isinstance_keys = []

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            models.storage.new(self)

            """check if there are no <kwargs> passed to the function"""
            return

        for key, value in kwargs.items():
            """looping over kwarg's elements"""
            
            """check if the  attribute exist in the BaseModel Class"""
            if key  == 'created_at':
                """convert the string to datetiem object"""
                my_time = datetime.datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f')
                self.created_at = my_time
            elif key == 'updated_at':
                my_time = datetime.datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f')
                self.updated_at = my_time

            else:
                """atherwise  just asign the value to the attribute"""

                if key != '__class__':
                    setattr(self, key, value)

            """push the key to the list <isinstance_keys>"""
            isinstance_keys.append(key)

        if 'created_at' not in isinstance_keys:
            """check if <created_at> in assained data or not"""
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            isinstance_keys.append('updated_at')
            isinstance_keys.append('created_at')
    
        if 'updated_at' not in isinstance_keys:
            """if there is no <updated_at>, copy the <create_at>"""
            self.updated_at = self.created_at
            isinstance_keys.append('updated_at')

        if 'id' not in isinstance_keys:
            """check if <id> in assained data or not"""
            self.id = str(uuid.uuid4())

    def __str__(self):
        """
        this is the constructor of the base class that not take
        any argumants and return object in dictionary representation
        """
        obj_dict = (self.__dict__).copy()
    
        return '[{}] ({}) {}'.\
        format(type(self).__name__, self.id, obj_dict)
    
    def save(self):
        """
        this function  it take
        a new value of updated_at as argumant and return nothing
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()
    
    def to_dict(self):
        """
        this function  it has no argumants and  returns 
        a dictionary containing all keys/values of __dict__ of the instance
        """
    def to_dict(self):
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key not in ['created_at', 'updated_at']:
                obj_dict[key] = value
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        
        return obj_dict




