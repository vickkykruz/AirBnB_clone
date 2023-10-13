#!/usr/bin/python3

"""
    This module contains one class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This class inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
