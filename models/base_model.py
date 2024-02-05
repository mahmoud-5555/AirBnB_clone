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
		self.created_at =  datetime.datetime.now()""" ?? iam not soure about this line"""
		self.updated_at = self.created_at
	
	def __str__():



