import unittest

from models.rectangle import Rectangle

class RectangleTestCase(unittest.TestCase):

    def test_passed_string_args(self):
        """test for value passed as a string"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_and_height_values(self):
        """test for wrong integer values"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area_of_a_rectangle(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
