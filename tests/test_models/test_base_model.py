#!/usr/bin/env python3
"""
    This is a test model that testing the atttibutes and method in the base
    model.
"""


import unittest
import datetime
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
        self.assetTrue(instClass,created_at == instClass.updated_at)
