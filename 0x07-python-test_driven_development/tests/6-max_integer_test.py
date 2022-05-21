#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Define a TestMaxInteger class that check if the max integer
    Attributes:
        None
    """
    def test_maxint_positive(self):
        """
        Check which is the max positive num in the list
        """
        self.assertEqual(max_integer([2, 3, 5, 9]), 9)
        self.assertEqual(max_integer([9, 3, 5, 2]), 9)
        self.assertEqual(max_integer([3, 9, 5, 2]), 9)
        self.assertEqual(max_integer([100, 34, 200]), 200)
        self.assertEqual(max_integer([9, 9, 9, 9]), 9)

    def test_maxint_negative(self):
        """
        Check which is the max negative num in the list
        """
        self.assertEqual(max_integer([-2, -3, -5, 4]), 4)
        self.assertEqual(max_integer([-2, -3, -1, -5]), -1)
        self.assertEqual(max_integer([-4, -4, -4, -4]), -4)

    def test_diferents_types_and_None(self):
        """
        Check which is the max num in the diferent types 
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer("abez10"), 'z')

    def test_errors(self):
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 4, 5, [2, 4, 5], 1])
        with self.assertRaises(TypeError):
            max_integer([1, 3, 4, {"i": 2, "x": 3}, 5])
