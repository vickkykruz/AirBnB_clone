#!/usr/bin/python3
"""
Place Module

This module contains the Place class, which inherits from the BaseModel class.
It defines a Place object with various attributes to represent a place for
renting, including name, description, number of rooms, number of bathrooms,
max guest capacity, price per night, location coordinates, and associated
amenity IDs.

Classes:
    - Place: Inherits from BaseModel and represents a place for renting.

Attributes:
    - city_id (str): The ID of the city where the place is located.
    - user_id (str): The ID of the user who owns the place.
    - name (str): The name of the place.
    - description (str): A description of the place.
    - number_rooms (int): The number of rooms in the place.
    - number_bathrooms (int): The number of bathrooms in the place.
    - max_guest (int): The maximum guest capacity.
    - price_by_night (int): The price per night for renting the place.
    - latitude (float): The latitude coordinate of the place's location.
    - longitude (float): The longitude coordinate of the place's location.
    - amenity_ids (list of str): IDs of amenities associated with the place.

Usage:
    To use this module, create instances of the Place class to represent
    different rental places and set their attributes accordingly.

"""


from models.base_model import BaseModel


class Place(BaseModel):
    """ This class inherits from the BaseModel class
            Attributes:
                name - holds the name of the user
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
