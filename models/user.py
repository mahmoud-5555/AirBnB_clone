#!/usr/bin/python3
"""the user module"""
from models import base_model

class User(base_model.BaseModel):
	"""the user calss , inherits from BaseModel"""
	email = ''
	password = ''
	first_name = ''
	last_name = ''
