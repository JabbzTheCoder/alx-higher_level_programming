#!/usr/bin/python3

'''The base class'''
class Base():
    """
    The base class for managing objects.

    Attributes:
    - __nb_objects: A class attribute to keep track of the number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
        - id: An optional parameter to set a specific ID for the object.

        If 'id' is not provided, it auto-increments the object's ID using the __nb_objects counter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
