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
		self.created_at =  datetime.datetime.now().isoformat()
		self.updated_at = self.created_at
	
	def __str__(self):
		"""
		this is the constructor of the base class that not take
		any argumants and return object in dictionary representation
		"""
		return '[] (<>) <>'.\
        format(type(self).__name__, self.id, self.__dict__)
	
	def save(self):
		"""
		this function  it take
		a new value of updated_at as argumant and return nothing
		"""
		self.updated_at = datetime.datetime.now().isoformat()
	
	def to_dict(self):
		"""
		this function  it has no argumants and  returns 
		a dictionary containing all keys/values of __dict__ of the instance
		"""
		obj_dict = self.__dict__
		obj_dict['__class__'] = self.__class__.__name__
		return obj_dict




