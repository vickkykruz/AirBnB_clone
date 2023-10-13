#!/usr/bin/python3

"""
    This module contains one class (State)
"""


from models.base_model import BaseModel


class State(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                name - holds the name of the state
    """
    name = ""
