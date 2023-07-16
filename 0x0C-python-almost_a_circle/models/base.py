#!/usr/bin/python3

"""defines a rectangle class."""

import json
import csv
import turtle


class Base:

    """defines base model for all other classes.
    Attributes: number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        """method to initialize a new Base.
        Args:
            id: identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """a method to return JSON serialization of list of dictionaries.
        Args:
            list_dictionaries: list of dictionaries.
        Returns:
            str: JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + ".json"
        l_dicts = [obj.to_dictionary() for obj in l_objs] if list_objs else []
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(l_dicts))

    @staticmethod
    def from_json_string(json_string):

        """a method write JSON serialization of list of objects.
        Args:
            list_objs: list of inherited instances
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """a method to return class instantces from a dict attributes.
        Args:
            **dictionary: pairs of attributes.
        Returns:
            Base: instance of the class
        """

        if dictionary and len(dictionary) > 0:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):

        """a method to return list classes instantces of JSON strings.
        Returns:
            list: list of classes
        """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):

        """a method to write the serialization list of objects to file.

        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if list_objs is None or len(list_objs) == 0:
                return
            if cls.__name__ == "Rectangle":
                writer.writerow(["id", "width", "height", "x", "y"])
                for e in list_objs:
                    writer.writerow([e.id, e.width, e.height, e.x, e.y])
            else:
                writer.writerow(["id", "size", "x", "y"])
                for e in list_objs:
                    writer.writerow([e.id, e.size, e.x, e.y])

    @classmethod
    def load_from_file_csv(cls):

        """a method to return list of classes from a CSV.

        """

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)

                return [
                    cls.create(**{k: int(v) for k, v in row.items()})
                    for row in reader]

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):

        """a method to draw Rectangles and Squares with turtle.

        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        def draw_shape(obj, color):
            turt.color(color)
            turt.showturtle()
            turt.up()
            turt.goto(obj.x, obj.y)
            turt.down()
            for _ in range(2):
                turt.forward(obj.width)
                turt.left(90)
                turt.forward(obj.height)
                turt.left(90)
            turt.hideturtle()

        for rect in list_rectangles:
            draw_shape(rect, "#ffffff")

        for sq in list_squares:
            draw_shape(sq, "#b5e3d8")
            turtle.exitonclick()
