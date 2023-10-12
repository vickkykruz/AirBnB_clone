#!/usr/bin/env python3
"""
    This is a test model that testing the atttibutes and method in the base
    model.
"""


import unittest
import datetime

import models
BaseModel = models.base_model.BaseModel

class TestBaseModel(unittest.TestCase):
    """ This is a class TestBaseModel that contains the attributes and methid
        for the functionality of the class
    """

    def test_initialization(self):
        """ This is a method that testes the intialization of the self
            attributes and value
        """
        instClass = BaseModel()
        self.assertIs(type(instClass), BaseModel)
        self.assertEqual(len(instClass.id), 36)
        self.assertTrue(type(instClass.updated_at) is datetime)
        self.assertTrue(type(instClass.created_at) is datetime)
        self.assetTrue(instClass.created_at == instClass.updated_at)
        
    def test_base(self):
        """This is a method that tests the base model"""
        instClass = BaseModel()
        instClass.name = "My First Model"
        instClass.my_number = 89
        
        self.assertTrue(type(instClass.id) is str)
        self.assertEqual(instClass.name, "My First Model")
        self.assertEqual(instClass.my_number, 89)
        
    def test_base_model_args(self):
        """ This is a test mothod that testes the *args"""
        instClass = BaseModel()
        
        # Testing that id exist and 2 or 1
        self.assertTrue(instClass.id is not None)
        self.assertTrue(instClass.id != 2)
        self.assertTrue(instClass.id != 1)
        
        # Testing that the created_at exist and is not 2 or 1
        self.assertTrue(instClass.created_at is not None)
        self.assertTrue(instClass.created_at != 2)
        self.assertTrue(instClass.created_at != 1)
        
        # Testing that the updated_at exist and is not a number
        self.assertTrue(instClass.updated_at is not None)
        self.assertTrue(instClass.updated_at != 2)
        self.assertTrue(instClass.updated_at != 1)
        
    def test_base_model_kwargs(self):
        """ This is a test model that tests the *kwargs """
        instClass = BaseModel()
        
        instClass__dir = instClass.to_dict()
        instClass2__dir = BaseModel(**instClass__dir)
        
        self.assertTrue(instClass__dir.id, instClass2__dir.id)
        self.assertTrue(instClass is not instClass2__dir)
        self.assertEqual(instClass.created_at, instClass2__dir.created_at)
        self.assertEqual(instClass.updated_at, instClass2__dir.updated_at)
        
    # This is a method that print __str__
    def test_base_model_str(self):
        """ This is a test model that tests the __str__ method """
        instClass = BaseModel()
        
        print_str = "[{}] ({}) {}".format(instClass.__class__.__name__, instClass.id, instClass.__dict__)
        self.assertEqual(instClass.__str__(), print_str)