#!/usr/bin/python3
"""Test max_integer.py
    Usage:
        max_integer(list[...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    """class that tests the function"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_integers(self):
        """Test Integers values"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([3, 2, 4, 1]), 4)
        self.assertEqual(max_integer([40, 50, 30]), 50)
        self.assertEqual(max_integer([200, 234, 453]), 453)

    def test_floats(self):
        """Test float values"""
        self.assertEqual(max_integer([1.5, 3.6, 3.4, 5.5]), 5.5)
        self.assertEqual(max_integer([0.3, 0.5, 0.4]), 0.5)
        self.assertEqual(max_integer([33.4, 33.1, 0.05, 12.0]), 33.4)
        self.assertEqual(max_integer([333.222, 435.594, 432.200, 12.44]),
                         435.594)
        self.assertEqual(max_integer([1.5, 0.3, 33.4, 333.222]), 333.222)

    def test_negatives(self):
        """Test negative values"""
        self.assertEqual(max_integer([-5, -3, -2, -8]), -2)
        self.assertEqual(max_integer([-0.2, -0.5, -4.4]), -0.2)
        self.assertEqual(max_integer([-11, -33, -5.3, -5.1]), -5.1)
        self.assertEqual(max_integer([-555, -1000, -312, -111]), -111)
        self.assertEqual(max_integer([-32, -22, -21, -11]), -11)

    def test_Large_numbers(self):
        """Test Large numbers"""
        self.assertEqual(max_integer([100000, 10000, 1111111, 1000]), 1111111)
        self.assertEqual(max_integer([200000, 300000, 100000, 10000]), 300000)
        self.assertEqual(max_integer([1_000_000, 100_000, 10_000]), 1_000_000)
        self.assertEqual(max_integer([1_000_000, 10_000, 100_000]), 1_000_000)
        self.assertEqual(max_integer([100_000, 10_000, 1_000_000]), 1_000_000)

    def test_numbers_collection(self):
        """Test all type of number"""
        self.assertEqual(max_integer([1, 1.5, -5, 100000]), 100000)
        self.assertEqual(max_integer([200000, 3, 0.3, -0.5]), 200000)
        self.assertEqual(max_integer([-20000, 8, 8.5, -32]), 8.5)
        self.assertEqual(max_integer([2000.2000, 654, 234, -31]), 2000.2000)
        self.assertEqual(max_integer([0.5, -5, -11, 5.5]), 5.5)

    def test_single_numbers(self):
        """test single numbers"""
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([54]), 54)
        self.assertEqual(max_integer([32]), 32)
        self.assertEqual(max_integer([3.3]), 3.3)
        self.assertEqual(max_integer([0]), 0)

    def test_strings(self):
        """Test list of strings"""
        list1 = ["hamza", "code", "programming", "bugs"]
        list2 = ["banana", "orange", "tomato", "ananas"]
        list3 = ["ar", "en", "fr", "sp"]
        list4 = ["1", "3", "4", "2"]
        list5 = ["#", "?", "!", "[]"]
        self.assertEqual(max_integer(list1), max(list1))
        self.assertEqual(max_integer(list2), max(list2))
        self.assertEqual(max_integer(list3), max(list3))
        self.assertEqual(max_integer(list4), max(list4))
        self.assertEqual(max_integer(list5), max(list5))

    def Test_booleans(self):
        """Test booleans"""
        self.assertTrue(max_integer([True, False]))
        self.assertTrue(max_integer([False, True]))


if __name__ == "__main__":
    unittest.main()
