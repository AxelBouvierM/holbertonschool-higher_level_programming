#!/usr/bin/python3
"""
Test for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test for Base class
    """

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(2)
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 2)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_failure(self):
        with self.assertRaises(TypeError):
            b5 = Base(2, 3)

        with self.assertRaises(ValueError):
            b6 = Base(-1)

        with self.assertRaises(ValueError):
            b7 = Base(0)

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 1}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_to_json_string(self):

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), "[{\"id\": 12}]")
