#!/usr/bin/python3
"""Define a class Base"""

import json
import csv
import os


class Base:
    """Defining class Base

    Attributes:
        __nb_objects (int): Private class attribute to keep track of
        the number of instances created.
        id (int): Public instance attribute to store the id of each instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new instance of class Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list represented by json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all aettributes set"""
        if cls.__name__ == "Rectangle":
            test = cls(1, 1)
        elif cls.__name__ == "Square":
            test = cls(1)
        else:
            test = None
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of instances to CSV format
        and writes it to a file
        """
        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            attrs = ["id", "width", "height", "x", "y"]
            attrs_vals = [0, 0, 0, 0, 0]
        else:
            attrs = ["id", "size", "x", "y"]
            attrs_vals = [0, 0, 0, 0]

        rows = []

        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                for key in range(len(attrs)):
                    attrs_vals[key] = obj.to_dictionary()[attrs[key]]
                rows.append(attrs_vals[:])

        with open(filename, "w") as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of instances from a CSV file"""
        filename = cls.__name__ + ".csv"

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as csv_file:
            read = csv.reader(csv_file)
            list_csv = list(read)

        if cls.__name__ == "Rectangle":
            attrs = ["id", "width", "height", "x", "y"]
        else:
            attrs = ["id", "size", "x", "y"]

        rows = []

        for elemt in list_csv:
            csv_dict = {}
            for key in enumerate(elemt):
                csv_dict[attrs[key[0]]] = int(key[1])
            rows.append(csv_dict)

        list_objs = []

        for i in range(len(rows)):
            list_objs.append(cls.create(**rows[i]))

        return list_objs
