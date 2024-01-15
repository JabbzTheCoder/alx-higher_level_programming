#!/usr/bin/python3
"""Base class for managing IDs and JSON serialization."""
import json

class Base:
    """Base class for managing IDs and JSON serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Args:
        - id (int): ID of the instance (default is None).

        Attributes:
        - id (int): ID of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
        - list_dictionaries (list): List of dictionaries.

        Returns:
        - str: JSON-formatted string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file in JSON format.

        Args:
        - list_objs (list): List of instances.

        Returns:
        - None
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        file_name = "{}.json".format(class_name)

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(file_name, "w") as file:
            file.write(json_string)
