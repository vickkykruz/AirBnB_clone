#!/usr/bin/python3
"""
    This module contains one class (Review)
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                place_id - place ID
    """
    place_id = ""
    user_id = ""
    text = ""
