#!/usr/bin/python3
"""
    This module contains one class (City)
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                name - holds the name of the city
                state_id - state id
    """
    state_id = ""
    name = ""
