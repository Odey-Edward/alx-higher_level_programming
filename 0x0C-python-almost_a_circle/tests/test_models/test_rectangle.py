import unittest
import sys
import inspect
from models import rectangle
from io import StringIO
from unittest.mock import patch

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

    def test_rectangle_display(self):
        expected_output = '####\n' * 6
        r1 = Rectangle(4, 6)
        
        with patch('sys.stdout', new_callable=StringIO) as mock_display:
            r1.display()

        output = mock_display.getvalue()
        self.assertEqual(expected_output, output)

    def test_rectangle_str_(self):
        expected_output = '[Rectangle] (12) 2/1 - 4/6\n'
        r = Rectangle(4, 6, 2, 1, 12)

        with patch('sys.stdout', new_callable=StringIO) as rectangle_string:
            print(r)

        output = rectangle_string.getvalue()
        self.assertEqual(expected_output, output)

    def test_rectangle_display2(self):
        r1_output = '\n\n' + '  ##\n' * 3
        r2_output = ' ###\n' * 2

        r1 = Rectangle(2, 3, 2, 2)
        r2 = Rectangle(3, 2, 1, 0)

        with patch('sys.stdout', new_callable=StringIO) as rectangle_display:
            r1.display()

        output = rectangle_display.getvalue()
        self.assertEqual(r1_output, output)

        with patch('sys.stdout', new_callable=StringIO) as rectangle_display:
            r2.display()

        output = rectangle_display.getvalue()
        self.assertEqual(r2_output, output)

    def test_rectangle_update(self):
        expected_output = '[Rectangle] (89) 4/10 - 2/3\n'

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)


        with patch('sys.stdout', new_callable=StringIO) as rectangle_update:
            print(r1)

        output = rectangle_update.getvalue()
        self.assertEqual(expected_output, output)

    def test_kwargs_rect_update(self):
        expected_output = '[Rectangle] (89) 1/3 - 4/2\n'

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, id=89, y=3, width=4)


        with patch('sys.stdout', new_callable=StringIO) as kwargs_update:
            print(r1)

        output = kwargs_update.getvalue()
        self.assertEqual(expected_output, output)

    def test_square_dictionary_represention(self):
        expected = "{'id': 14, 'width': 10, 'height': 2, 'x': 1, 'y': 9}\n"

        r1 = Rectangle(10, 2, 1, 9)
        result = r1.to_dictionary()

        with patch('sys.stdout', new_callable=StringIO) as actual_output:
            print(result)

        self.assertEqual(expected, actual_output.getvalue())

    def test_module_docstring(self):
        self.assertTrue(len(rectangle.__doc__) > 1)
    
    def test_class_docstring(self):
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_function_docstring(self):
        functions = inspect.getmembers(Rectangle, inspect.isfunction)

        for function in functions:
            self.assertTrue(len(function[1].__doc__) > 1)
