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

    def __init__(self, *args, **kwargs):
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

        if kwargs is {}:
            """check if there are no <kwargs> passed to the function"""
            self.__init__()
            return

        for key, value in kwargs.items():
            """looping over kwarg's elements"""
            if hasattr(self, key):
                """check if the  attribute exist in the BaseModel Class"""
                if key  == 'created_at' or key == 'updated_at':
                    """convert the string to datetiem object"""
                    my_time = datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, my_time)
                else:
                    """atherwise  just asign the value to the attribute"""
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
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))



