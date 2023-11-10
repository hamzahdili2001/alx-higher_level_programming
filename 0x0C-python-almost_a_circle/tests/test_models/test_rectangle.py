#!/usr/bin/python3
"""Tests Rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_Init(unittest.TestCase):
    """Test init for the Rectangle class"""

    def test_rectangle_instance(self):
        """check if rectangle class isinstance of Base"""
        self.assertIsInstance(Rectangle(10, 10), Base)

    def test_rectangle_args(self):
        """test one and no args"""
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_rectangle_two_args(self):
        """Test two args"""
        r1 = Rectangle(10, 10)
        r2 = Rectangle(20, 12)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_tree_args(self):
        """Test four args"""
        r1 = Rectangle(12, 23, 3)
        r2 = Rectangle(32, 21, 22)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_four_args(self):
        """Test four args"""
        r1 = Rectangle(12, 23, 21, 4)
        r2 = Rectangle(22, 32, 32, 21)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_five_args(self):
        """Test five args"""
        r1 = Rectangle(22, 76, 33, 3, 7)
        self.assertEqual(r1.id, 7)

    def test_rectangle_more_than_five_args(self):
        """Test More than five args"""
        with self.assertRaises(TypeError):
            Rectangle(12, 23, 33, 32, 1, 12)

        with self.assertRaises(TypeError):
            Rectangle(12, 44, 32, 3, 34, 32, 23)

    def test_rectangle_width_private(self):
        """Test width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 0, 4, 4, 5).__width)

    def test_rectangle_height_private(self):
        """Test height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 0, 4, 4, 5).__height)

    def test_rectangle_x_private(self):
        """Test x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 0, 4, 4, 5).__x)

    def test_rectangle_y_private(self):
        """Test y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 0, 4, 4, 5).__y)

    def test_rectangle_width_setter(self):
        """test width setter"""
        r = Rectangle(12, 22, 32, 21, 7)
        r.__width = 18
        self.assertEqual(r.__width, 18)

    def test_rectangle_height_setter(self):
        """test heigth setter"""
        r = Rectangle(12, 22, 32, 21, 7)
        r.__height = 18
        self.assertEqual(r.__height, 18)

    def test_rectangle_x_setter(self):
        """test x setter"""
        r = Rectangle(12, 22, 32, 21, 7)
        r.__x = 18
        self.assertEqual(r.__x, 18)

    def test_rectangle_y_setter(self):
        """test y setter"""
        r = Rectangle(12, 22, 32, 21, 7)
        r.__y = 18
        self.assertEqual(r.__y, 18)

    def test_rectangle_id_setter(self):
        """test id setter"""
        r = Rectangle(12, 22, 32, 21, 7)
        r.id = 18
        self.assertEqual(r.id, 18)

    def test_rectangle_width_getter(self):
        """test width getter"""
        r = Rectangle(12, 22, 32, 21, 7)
        self.assertEqual(r.width, 12)

    def test_rectangle_height_getter(self):
        """test height getter"""
        r = Rectangle(12, 22, 32, 21, 7)
        self.assertEqual(r.height, 22)

    def test_rectangle_x_getter(self):
        """test x getter"""
        r = Rectangle(12, 22, 32, 21, 7)
        self.assertEqual(r.x, 32)

    def test_rectangle_y_getter(self):
        """test y getter"""
        r = Rectangle(12, 22, 32, 21, 7)
        self.assertEqual(r.y, 21)

    def test_rectangle_id_getter(self):
        """test id getter"""
        r = Rectangle(12, 22, 32, 21, 7)
        self.assertEqual(r.id, 7)

    def test_rectangle_width_getter(self):
        """test width getter"""
        r = Rectangle(12, 22, 32, 21, 7)
        self.assertEqual(r.__width, 12)


class TestRectangle_width(unittest.TestCase):
    """Test rectangle width"""

    def test_None_width(self):
        """Test for None Value"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(None, 1)

    def test_str_width(self):
        """Test for str width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle("str", 1)

    def test_bytes_width(self):
        """Test for bytes width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(b"binary", 1)

    def test_list_width(self):
        """Test for list width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle([1, 2, 3], 1)

    def test_bool_width(self):
        """Test for bool width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(True, 1)

    def tests_float_width(self):
        """Test for float width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(3.4, 1)

    def test_tuple_width(self):
        """Test for tuple width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle((1, 2, 3), 1)

    def test_dict_width(self):
        """Test for dict width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle({1: "Hamza"}, 1)

    def test_complex_width(self):
        """Test for complex width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(complex("hamza"), 1)

    def test_frozenset_width(self):
        """Test for frozenset width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 4}), 1)

    def test_range_width(self):
        """Test for range width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(range(10), 1)

    def test_bytearray_width(self):
        """Test for bytearray width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(bytearray(b"bytes"), 1)

    def test_memoryview_width(self):
        """Test for memoryview width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(memoryview(b"bytes"), 1)

    def test_inf_width(self):
        """Test for inf width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(float("inf"), 1)

    def test_nan_width(self):
        """Test for nan width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(float("nan"), 1)

    def test_negative_width(self):
        """Test for negative width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(-1, 1)

    def test_zero_width(self):
        """Test for negative width"""
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(0, 1)


if __name__ == "__main__":
    unittest.main()
