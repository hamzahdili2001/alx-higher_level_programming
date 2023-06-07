#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer([..])
    """
    def regular_test(self):
        """Regular Tests"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([33, 40, 50, -20]), 50)
        self.assertEqual(max_integer([1000, -2000, 4000, 1500]), 4000)

    def empty_list(self):
        """Empty List Test"""
        self.assertIsNone(max_integer([]))

    def string_test(self):
        """String Tests"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['c', 'b', 'a']), 'c')

    def float_test(self):
        """Float Tests"""
        self.assertEqual(max_integer([1.4, 1.5, 1.9]), 1.9)
        self.assertEqual(max_integer([55.3, 1.3, 1.03]), 55.3)
        self.assertEqual(max_integer(-2.4, -3.5, -2.1), -2.1)

    def mixed_test(self):
        """Mixed Tests"""
        self.assertEqual(max_integer([1, '4', 2.5]), TypeError)
        self.assertEqual(max_integer(["School", 33, -2.3]), TypeError)


if __name__ == '__main__':
    unittest.main()
