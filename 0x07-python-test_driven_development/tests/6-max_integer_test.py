#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests"""
    def test_empty_list(self):
        """test_empty_list"""
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        """test_positive_numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """test_negative_numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """test_mixed_numbers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-10, 0, 10]), 10)
        self.assertEqual(max_integer([-10, -5, 0]), 0)

    def test_single_element_list(self):
        """test_mixed_numbers"""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-100]), -100)
        self.assertEqual(max_integer([0]), 0)

    def test_large_numbers(self):
        """test_large_numbers"""
        self.assertEqual(max_integer([1_000_000, 100_000, 10_000]), 1_000_000)
        self.assertEqual(max_integer([1_000_000, 10_000, 100_000]), 1_000_000)
        self.assertEqual(max_integer([100_000, 10_000, 1_000_000]), 1_000_000)

    def test_float_numbers(self):
        """test_float_numbers"""
        self.assertAlmostEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
        self.assertAlmostEqual(max_integer([3.3, 2.2, 1.1]), 3.3)

    def test_string_values(self):
        """test_string_values"""
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')
        self.assertEqual(max_integer(['zebra', 'lion', 'elephant']), 'zebra')

    def test_boolean_values(self):
        """test_boolean_values"""
        self.assertTrue(max_integer([True, False]))
        self.assertTrue(max_integer([False, True]))


if __name__ == '__main__':
    unittest.main()
