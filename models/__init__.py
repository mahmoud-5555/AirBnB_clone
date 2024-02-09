#!/usr/bin/python3
"""this the files configration"""
from models.engine.file_storage import FileStorage
from . import base_model
from . import user
from . import state
from . import city
from . import amenity
from . import place
from . import review
import re


storage = FileStorage()
storage.reload()
__all__ = ['base_model', 'user', 'state',
           'city',  'amenity', 'place', 'review']


def sp_quotes(string):
    """this function used in make split to the lines"""
    pattern = r'(?:[^\s,"]|"(?:\\.|[^"])*")+'
    matches = re.findall(pattern, string)
    return [match.strip('"\'') for match in matches]
