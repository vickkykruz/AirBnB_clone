import unittest
from models.state import State
from models import storage
from datetime import datetime
import os


class StateTest(unittest.TestCase):
    """ This is a model that holds the yest cases for class State """

    def test_state_model(self):
        """ This is a model the test the attribute by default """

        state1 = State()

        self.assertEqual(len(state1.id), 36)
        self.assertTrue(type(state1.created_at) is datetime)
        self.assertTrue(type(state1.updated_at) is  datetime)
        self.assertTrue(type(state1.name) is str)
        self.assertTrue(state1.created_at == state1.updated_at)

    def test_state_model_two(self):
        """ This is a model that test the value by default """
        state1 = State()

        self.assertEqual(state1.name, "")

    def test_state_model_three(self):
        """ This is a model that test the input value by the user """

        state1 = State()
        state1.name = "new_state"

        self.assertEqual(state1.name, "new_state")
        self.assertEqual(type(state1.name) is str)
