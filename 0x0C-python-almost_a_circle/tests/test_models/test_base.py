#!/usr/bin/python3
"""
Unit tests for the classes and methods in the models package.
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):

    """
    Unit tests for testing instantiation of the Base class.
    """

    def test_no_arg(self):
        """
        Test instantiation of Base class with no arguments.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_instances_after_unique_id(self):
        """
        Test the number of instances after instantiation with a unique id.
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """
        Test the id attribute is public and can be modified.
        """
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """
        Test the __nb_instances attribute is private and cannot be accessed.
        """
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """
        Test instantiation of Base class with a string id.
        """
        self.assertEqual("school", Base("school").id)

    def test_float_id(self):
        """
        Test instantiation of Base class with a float id.
        """
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        """
        Test instantiation of Base class with a complex number id.
        """
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        """
        Test instantiation of Base class with a dictionary id.
        """
        self.assertEqual({"air": 1, "beg": 2}, Base({"air": 1, "beg": 2}).id)

    def test_bool_id(self):
        """
        Test instantiation of Base class with a boolean id.
        """
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """
        Test instantiation of Base class with a list id.
        """
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        """
        Test instantiation of Base class with a tuple id.
        """
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        """
        Test instantiation of Base class with a set id.
        """
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        """
        Test instantiation of Base class with a frozenset id.
        """
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        """
        Test instantiation of Base class with a range id.
        """
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        """
        Test instantiation of Base class with a bytes id.
        """
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        """
        Test instantiation of Base class with a bytearray id.
        """
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        """
        Test instantiation of Base class with a memoryview id.
        """
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        """
        Test instantiation of Base class with an infinite float id.
        """
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """
        Test instantiation of Base class with a NaN float id.
        """
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """
        Test instantiation of Base class with two arguments (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            Base(1, 2)
   
     def test_three_bases(self):
        """
        Test instantiation of Base class with three instances.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """
        Test instantiation of Base class with None as id argument.
        """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """
        Test instantiation of Base class with a unique id.
        """
        self.assertEqual(12, Base(12).id)
      

class TestBaseToJsonString(unittest.TestCase):
    """
    Unit tests for testing to_json_string method of Base class.
    """

    def test_to_json_string_square_one_dict(self):
        """
        Test to_json_string with a list containing one Square dictionary.
        """
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        """
        Test to_json_string with a list containing two Square dictionaries.
        """
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        """
        Test to_json_string with an empty list.
        """
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_None(self):
        """
        Test to_json_string with None.
        """
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_rectangle_type(self):
        """
        Test the return type of to_json_string for Rectangle objects.
        """
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """
        Test to_json_string with a list containing one Rectangle dictionary.
        """
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        """
        Test to_json_string with a list containing two Rectangle dictionaries.
        """
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        """
        Test the return type of to_json_string for Square objects.
        """
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))



class TestBaseFromJsonString(unittest.TestCase):
    """
    Unit tests for testing from_json_string method of Base class.
    """

    def test_from_json_string_square_two_dicts(self):
        """
        Test from_json_string with a JSON string containing two Square dictionaries.
        """
        json_string = '[{"id": 89, "size": 10}, {"id": 7, "size": 1}]'
        square_list = Square.from_json_string(json_string)
        self.assertEqual(7, square_list[1].id)

    def test_from_json_string_empty_string(self):
        """
        Test from_json_string with an empty string.
        """
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_None(self):
        """
        Test from_json_string with None.
        """
        self.assertEqual([], Base.from_json_string(None))


       def test_from_json_string_rectangle_type(self):
        """
        Test the return type of from_json_string for Rectangle objects.
        """
        json_string = '[{"id": 89, "width": 10, "height": 4}]'
        self.assertEqual(list, type(Base.from_json_string(json_string)))

    def test_from_json_string_rectangle_one_dict(self):
        """
        Test from_json_string with a JSON string containing one Rectangle dictionary.
        """
        json_string = '[{"id": 89, "width": 10, "height": 4}]'
        rect_list = Rectangle.from_json_string(json_string)
        self.assertEqual(89, rect_list[0].id)

    def test_from_json_string_rectangle_two_dicts(self):
        """
        Test from_json_string with a JSON string containing two Rectangle dictionaries.
        """
        json_string = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        rect_list = Rectangle.from_json_string(json_string)
        self.assertEqual(7, rect_list[1].id)

    def test_from_json_string_square_type(self):
        """
        Test the return type of from_json_string for Square objects.
        """
        json_string = '[{"id": 89, "size": 10}]'
        self.assertEqual(list, type(Base.from_json_string(json_string)))

    def test_from_json_string_square_one_dict(self):
        """
        Test from_json_string with a JSON string containing one Square dictionary.
        """
        json_string = '[{"id": 89, "size": 10}]'
        square_list = Square.from_json_string(json_string)
        self.assertEqual(10, square_list[0].size)


class TestBaseSaveToFile(unittest.TestCase):
    """
    Unit tests for testing save_to_file method of Base class.
    """

    @classmethod
    def tearDownClass(cls):
OBOBOB        """
OBOBOB        Clean up any created files after running the tests.
OBOBOB        """
OBOBOB        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
OBOBOB        except FileNotFoundError:
OBOBOB            pass
OBOBOB

    def test_save_to_file_no_arguments(self):
        """
        Test saving without providing a list of objects (should raise TypeError).
        """
        with self.assertRaises(TypeError):
OBOBOB            Base.save_to_file()
OBOBOBOBOBOBOBOBOBOBOBOB
OBOBOB    def test_save_to_file_extra_argument(self):
        """
        Test saving with an extra argument (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            Base.save_to_file([], 123)
OBOBOBOBOBOB

OAOAOAOAOAOAOAOAOAOAOAOAOAOAOA     def test_save_to_file_rectangle(self):
        """
        Test saving a list of Rectangle objects to a file.
        """
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
OBOBOBOBOBOB        Rectangle.save_to_file([r1, r2])
OBOBOB        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_save_to_file_square(self):
        """
        Test saving a list of Square objects to a file.
        """
OBOBOB        s1 = Square(10, 2, 3, 4)
OBOBOB        s2 = Square(4, 5, 21, 2)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.isfile("Square.json"))

    def test_save_to_file_empty_list(self):
        """
        Test saving an empty list to a file.
OBOBOB        """
        Base.save_to_file([])
OBOBOBOBOBOB        self.assertTrue(os.path.isfile("Base.json"))
OBOBOB
    def test_save_to_file_None(self):
        """
        Test saving None to a file (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            Base.save_to_file(None)
OBOBOBOBOBOBOBOBOB
OBOBOB

class TestBaseCreate(unittest.TestCase):
    """
    Unit tests for testing create method of Base class.
    """

    def test_create_extra_args(self):
OBOBOB        """
OBOBOB        Test creating an object using the create method with extra arguments (should raise TypeError).
OBOBOB        """
        with self.assertRaises(TypeError):
            Base.create(id=1, name="John")

    def test_create_invalid_kwargs(self):
        """
        Test creating an object using the create method with invalid keyword arguments (should raise TypeError).
OBOBOBOBOBOBOBOBOBOBOBOBOBOBOB        """
        with self.assertRaises(TypeError):
            Base.create(width=10, height=5)

    def test_create_invalid_args(self):
        """
OBOBOB        Test creating an object using the create method with invalid arguments (should raise TypeError).
OBOBOBOBOBOBOBOBOBOBOBOB        """
        with self.assertRaises(TypeError):
            Base.create(10, 5)

    def test_create_rectangle(self):
        """
OBOBOB        Test creating a Rectangle object using the create method.
OBOBOBOBOBOBOBOBOB        """
OBOBOB        rectangle_dict = {'id': 1, 'width': 10, 'height': 5}
        r = Rectangle.create(**rectangle_dict)
        self.assertEqual("[Rectangle] (1) 0/0 - 10/5", str(r))

    def test_create_square(self):
        """
        Test creating a Square object using the create method.
OBOBOBOBOBOB        """
OBOBOB        square_dict = {'id': 7, 'size': 5}
        s = Square.create(**square_dict)
        self.assertEqual("[Square] (7) 0/0 - 5", str(s))

    def test_create_no_args(self):
        """
        Test creating an object using the create method without any arguments (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            Base.create()


class TestBaseLoadFromFile(unittest.TestCase):
    """
    Unit tests for testing load_from_file method of Base class.
    """

    @classmethod
    def tearDownClass(cls):
        """
        Clean up any created files after running the tests.
        """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_load_from_file_square(self):
        """
        Test loading Square objects from a file.
        """
        s1 = Square(5, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        Square.save_to_file([s1, s2])
        obj_list = Square.load_from_file()
        self.assertEqual(str(s1), str(obj_list[0]))

    def test_load_from_file_incorrect_type(self):
        """
        Test loading objects of incorrect type from a file.
        """
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        obj_list = Square.load_from_file()
        self.assertEqual([], obj_list)

    def test_load_from_file_rectangle(self):
        """
        Test loading Rectangle objects from a file.
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        obj_list = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(obj_list[0]))

    def test_load_from_file_empty_file(self):
        """
        Test loading from an empty file.
        """
        self.assertEqual([], Base.load_from_file())

    def test_load_from_file_file_not_found(self):

        """
        Test loading from a non-existent file.
        """
        self.assertEqual([], Base.load_from_file())


if __name__ == '__main__':
    unittest.main()

