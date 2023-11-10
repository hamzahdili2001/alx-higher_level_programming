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
        r2 = Rectangle(12, 20)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_tree_args(self):
        """Test four args"""
        r1 = Rectangle(3, 12, 23)
        r2 = Rectangle(22, 32, 21)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_four_args(self):
        """Test four args"""
        r1 = Rectangle(4, 12, 23, 21)
        r2 = Rectangle(21, 22, 32, 32)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_five_args(self):
        """Test five args"""
        r1 = Rectangle(7, 22, 76, 33, 3)
        self.assertEqual(r1.id, 3)

    def test_rectangle_more_than_five_args(self):
        """Test More than five args"""
        with self.assertRaises(TypeError):
            Rectangle(12, 12, 23, 33, 32, 1)

        with self.assertRaises(TypeError):
            Rectangle(23, 12, 44, 32, 3, 34, 32)

    def test_rectangle_width_private(self):
        """Test width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 1, 0, 4, 4).__width)

    def test_rectangle_height_private(self):
        """Test height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 1, 0, 4, 4).__height)

    def test_rectangle_x_private(self):
        """Test x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 1, 0, 4, 4).__x)

    def test_rectangle_y_private(self):
        """Test y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 1, 0, 4, 4).__y)

    def test_rectangle_width_setter(self):
        """test width setter"""
        r = Rectangle(7, 12, 22, 32, 21)
        r.width = 18
        self.assertEqual(r.width, 18)

    def test_rectangle_height_setter(self):
        """test heigth setter"""
        r = Rectangle(7, 12, 22, 32, 21)
        r.height = 18
        self.assertEqual(r.height, 18)

    def test_rectangle_x_setter(self):
        """test x setter"""
        r = Rectangle(7, 12, 22, 32, 21)
        r.x = 18
        self.assertEqual(r.x, 18)

    def test_rectangle_y_setter(self):
        """test y setter"""
        r = Rectangle(7, 12, 22, 32, 21)
        r.y = 18
        self.assertEqual(r.y, 18)

    def test_rectangle_id_setter(self):
        """test id setter"""
        r = Rectangle(7, 12, 22, 32, 21)
        r.id = 18
        self.assertEqual(r.id, 18)

    def test_rectangle_width_getter(self):
        """test width getter"""
        r = Rectangle(7, 12, 22, 32, 21)
        self.assertEqual(r.width, 7)

    def test_rectangle_height_getter(self):
        """test height getter"""
        r = Rectangle(7, 12, 22, 32, 21)
        self.assertEqual(r.height, 12)

    def test_rectangle_x_getter(self):
        """test x getter"""
        r = Rectangle(7, 12, 22, 32, 21)
        self.assertEqual(r.x, 22)

    def test_rectangle_y_getter(self):
        """test y getter"""
        r = Rectangle(7, 12, 22, 32, 21)
        self.assertEqual(r.y, 32)

    def test_rectangle_id_getter(self):
        """test id getter"""
        r = Rectangle(7, 12, 22, 32, 21)
        self.assertEqual(r.id, 21)


class TestRectangle_width(unittest.TestCase):
    """Test rectangle width"""

    def test_None_width(self):
        """Test for None Value"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 1)

    def test_str_width(self):
        """Test for str width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("str", 1)

    def test_bytes_width(self):
        """Test for bytes width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"hamza", 1)

    def test_list_width(self):
        """Test for list width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 1)

    def tests_float_width(self):
        """Test for float width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.4, 1)

    def test_tuple_width(self):
        """Test for tuple width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 1)

    def test_dict_width(self):
        """Test for dict width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1: "hamza"}, 1)

    def test_complex_width(self):
        """Test for complex width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(6), 1)

    def test_frozenset_width(self):
        """Test for frozenset width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 1)

    def test_range_width(self):
        """Test for range width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(100), 1)

    def test_bytearray_width(self):
        """Test for bytearray width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b"array"), 1)

    def test_memoryview_width(self):
        """Test for memoryview width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b"view"), 1)

    def test_inf_width(self):
        """Test for inf width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 1)

    def test_nan_width(self):
        """Test for nan width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("nan"), 1)

    def test_negative_width(self):
        """Test for negative width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)

    def test_zero_width(self):
        """Test for negative width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)


class TestRectangle_height(unittest.TestCase):
    """Test rectangle height"""

    def test_None_height(self):
        """Test for None Value"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        """Test for str height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "str")

    def test_bytes_height(self):
        """Test for bytes height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b"hamza")

    def test_list_height(self):
        """Test for list height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def tests_float_height(self):
        """Test for float height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1.4)

    def test_tuple_height(self):
        """Test for tuple height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_dict_height(self):
        """Test for dict height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1: "hamza"})

    def test_complex_height(self):
        """Test for complex height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(6))

    def test_frozenset_height(self):
        """Test for frozenset height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3}))

    def test_range_height(self):
        """Test for range height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(100))

    def test_bytearray_height(self):
        """Test for bytearray height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b"array"))

    def test_memoryview_height(self):
        """Test for memoryview height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b"view"))

    def test_inf_height(self):
        """Test for inf height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("inf"))

    def test_nan_height(self):
        """Test for nan height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("nan"))

    def test_negative_height(self):
        """Test for negative height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        """Test for negative height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


if __name__ == "__main__":
    unittest.main()
