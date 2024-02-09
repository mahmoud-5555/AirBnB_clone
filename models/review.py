#!/usr/bin/python3
"""the Review module"""
from models import base_model


class Review(base_model.BaseModel):
    """
    Review class contains attributes and methods
    for the review table in the database
    """
    place_id = ''
    user_id = ''
    text = ''
