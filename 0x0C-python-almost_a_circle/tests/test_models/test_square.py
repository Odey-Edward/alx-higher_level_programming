import sys
import unittest
import inspect

from unittest.mock import patch
from io import StringIO
from models.square import Square
from models import square

class TestSuite_for_Square(unittest.TestCase):
    
    def test_square_str_(self):
        s1_output = '[Square] (5) 1/3 - 3\n'
        s2_output = '[Square] (9) 1/3 - 3\n'

        s1 = Square(3, 1, 3, 5)
        s2 = Square(3, 1, 3, 9)

        with patch('sys.stdout', new_callable=StringIO) as s1_actual_output:
            print(s1)

        with patch('sys.stdout', new_callable=StringIO) as s2_actual_output:
            print(s2)

        self.assertEqual(s1_output, s1_actual_output.getvalue())
        self.assertEqual(s2_output, s2_actual_output.getvalue())

    def test_square_area(self):

        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s4 = Square(40)

        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)
        self.assertEqual(s4.area(), 1600)

    def test_square_display(self):
        s1_output = '#####\n' * 5
        s2_output = '#########\n' * 9
        s3_output = '\n' * 3 + ' ###\n' * 3

        s1 = Square(5)
        s2 = Square(9)
        s3 = Square(3, 1, 3)


        with patch('sys.stdout', new_callable=StringIO) as s1_actual_output:
            s1.display()

        with patch('sys.stdout', new_callable=StringIO) as s2_actual_output:
            s2.display()

        with patch('sys.stdout', new_callable=StringIO) as s3_actual_output:
            s3.display()

        self.assertEqual(s1_output, s1_actual_output.getvalue())
        self.assertEqual(s2_output, s2_actual_output.getvalue())
        self.assertEqual(s3_output, s3_actual_output.getvalue())

    def test_wrong_square_attribute(self):
        s1 = Square(5)

        with self.assertRaises(TypeError):
            s1.size = '9'

        with self.assertRaises(ValueError):
            s1.size = -56

    def test_square_update(self):
        expected_output = '[Square] (89) 12/1 - 7\n'

        s1 = Square(5)
        s1.update(size=7, x=12, id=89, y=1)

        with patch('sys.stdout', new_callable=StringIO) as square_output:
            print(s1)

        self.assertEqual(expected_output, square_output.getvalue())

        s1.update(1, 2, 3, 4)
        expected_output = '[Square] (1) 3/4 - 2\n'

        with patch('sys.stdout', new_callable=StringIO) as square_output:
            print(s1)

        self.assertEqual(square_output.getvalue(), expected_output)

    def test_to_dictionary(self):
        expected_value = {'id': 1, 'size': 10, 'x': 2, 'y': 1}

        s1 = Square(10, 2, 1, 1)
        s1_dictionary = s1.to_dictionary()

        self.assertEqual(s1_dictionary, expected_value)

    def test_module_docstring(self):
        self.assertTrue(len(square.__doc__) > 1)
    
    def test_class_docstring(self):
        self.assertTrue(len(Square.__doc__) > 1)

    def test_function_docstring(self):
        functions = inspect.getmembers(Square, inspect.isfunction)

        for function in functions:
            self.assertTrue(len(function[1].__doc__) > 1)
