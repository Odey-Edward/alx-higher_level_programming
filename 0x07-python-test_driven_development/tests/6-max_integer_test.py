#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class for Max_integer"""


    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)
        self.assertEqual(max_integer([1, 3, -4, 2]), 3)
        self.assertEqual(max_integer([-1, -8, -4, -2]), -1)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)


