#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of attributes and methods of the given object using the dir() function.

    Args:
    - obj: any object

    Returns:
    - list: a list of attribute and method names of the object
    """

    return dir(obj)