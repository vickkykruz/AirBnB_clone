#!/usr/bin/python3
"""
    This module contains one class (Amenity)
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                name - holds the name of the amenity
    """
    name = ""
