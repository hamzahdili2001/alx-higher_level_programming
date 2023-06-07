#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])."""

    def list(self):
        """Test an ordered list"""

        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def unordered_list(self):
        """Test an unordered list"""

        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def max(self):
        """Test with max value."""

        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def empty_list(self):
        """Test empty list."""

        empty = []
        self.assertEqual(max_integer(empty), None)

    def one_number_list(self):
        """Test single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_float(self):
        """Test float."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def mixed_test(self):
        """Test list of int and float."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Hamza"
        self.assertEqual(max_integer(string), 'z')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Hamza", "is", "cool"]
        self.assertEqual(max_integer(strings), 'is')

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
