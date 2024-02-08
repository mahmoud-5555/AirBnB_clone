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
	__file_path = 'file.json'
	__objects = {}

	def all(self):
		"""returns the dictionary"""
		return self.__objects
	
	def new(self, opj):
		""": sets in <__objects> the <obj> with key <obj class name>.id"""
		self.__objects[opj.id] = opj.to_dict()

	def save(self):
		with open(self.__file_path,'w+', encoding='UTF-8') as json_file:
			json.dump(self.__objects, json_file, indent=2)
	

	def reload(self):
		with open(self.__file_path,'w+',encoding='UTF-8') as json_file:
			if json_file.read():
				print(json.load(json_file, indent=2))

