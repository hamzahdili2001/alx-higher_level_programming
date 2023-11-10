#!/usr/bin/python3
"""Tests for Base class"""

import unittest
from models.base import Base


class Test_Base_Init(unittest.TestCase):
    """Test init for Base class"""

    def test_types_instance(self):
        """test types and instances"""
        b1 = Base()
        b2 = Base()
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b2, Base)
        self.assertFalse(type(b1) is type(Base))
        self.assertTrue(type(b1) is type(b2))
        self.assertFalse(id(b1) == id(b2))
        self.assertFalse(id(b1) == id(Base))

    def test_no_argument(self):
        """Test no args"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 2)

    def test_base_counts(self):
        """Test Counts of the base"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        b4 = Base()
        self.assertEqual(b4.id, b1.id + 3)

    def test_none_id(self):
        """Test None id"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id(self):
        """Tests unique id"""
        self.assertEqual(12, Base(12).id)
        b1 = Base(22)
        self.assertEqual(b1.id, 22)

    def test_instances_after_id(self):
        """Test instances after the unique id"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_public_id(self):
        """Test public id"""
        b1 = Base(15)
        b1.id = b1.id - 5
        self.assertEqual(b1.id, 10)
        b2 = Base(10)
        b2.id = 12
        self.assertEqual(b2.id, 12)

    def test_private_instance(self):
        """Test private instance"""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instance)

    def test_string_as_id(self):
        """Test strings"""
        b1 = Base("hamza")
        self.assertEqual("hamza", b1.id)
        b2 = Base("12")
        self.assertEqual("12", b2.id)

    def test_float_as_id(self):
        """Test float"""
        b1 = Base(0.0)
        self.assertEqual(b1.id, 0.0)
        b2 = Base(0)
        b2.id = b1.id + 1.1
        self.assertEqual(b2.id, 1.1)

    def test_complex_as_id(self):
        """Test complex id"""
        self.assertEqual(Base(complex(12)).id, complex(12))

    def test_dict_as_id(self):
        """Test dict id"""
        self.assertEqual(Base({1: "hamza"}).id, {1: "hamza"})

    def test_list_as_id(self):
        """Test list id"""
        self.assertEqual(Base([1, 2, 3, 5]).id, [1, 2, 3, 5])

    def test_bool_as_id(self):
        """Test bool id"""
        self.assertEqual(Base(True).id, True)
        self.assertEqual(Base(not True).id, False)

    def test_tuple_as_id(self):
        """Test tuple id"""
        self.assertEqual(Base((1, 2, 3, 4)).id, (1, 2, 3, 4))

    def test_set_as_id(self):
        """Test tuple id"""
        self.assertEqual(Base({1, 2, 3, 4}).id, {1, 2, 3, 4})

    def test_range_as_id(self):
        """Test range id"""
        self.assertEqual(Base(range(10)).id, range(10))

    def test_bytes_as_id(self):
        """Test bytes id"""
        self.assertEqual(Base(b"hamza").id, b"hamza")

    def test_bytearray_as_id(self):
        self.assertEqual(bytearray(b"hamza"), Base(bytearray(b"hamza")).id)

    def test_memoryview_as_id(self):
        self.assertEqual(memoryview(b"hamza"), Base(memoryview(b"hamza")).id)

    def test_inf_as_id(self):
        self.assertEqual(float("inf"), Base(float("inf")).id)

    def test_NaN_as_id(self):
        self.assertNotEqual(float("nan"), Base(float("nan")).id)

    def test_two_as_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
