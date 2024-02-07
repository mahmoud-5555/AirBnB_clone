#!/usr/bin/python3
"""
this file will be response
of convert opject to json and
save it to file
"""
import json


class FileStorage:
	"""
	the class <FileStorage>
	class that response of  save object to a
	.json file.
	"""
	__file_path = ''
	__objects = {}

	def __init__(self, path):
		self.__file_path = path

	def all(self):
		"""returns the dictionary"""
		return self.__objects
	
	def new(self, opj):
		""": sets in <__objects> the <obj> with key <obj class name>.id"""
		self.__objects.update({opj.id : opj.to_dict})

	def save(self):
		with open(self.__file_path,'a+') as json_file:
			json.dump(self.__objects, json_file)
			self.__objects.clear()

	def reload(self):
		with open(self.__file_path, 'r+') as json_file:
			self.__objects.update(json.load(json_file))

