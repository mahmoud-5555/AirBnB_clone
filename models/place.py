#!/usr/bin/python3
"""the Place module"""
from models import base_model


class Place(base_model.BaseModel):
	"""this is Place class"""
	city_id = ''
	user_id = ''
	name = ''
	description = ''
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0.0
	longitude = 0.0
	amenity_ids = []
