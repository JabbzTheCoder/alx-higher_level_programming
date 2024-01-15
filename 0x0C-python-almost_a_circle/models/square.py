#!/usr/bin/python3
"""Defines a squar class."""
from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size,x,y,id)
    
    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """Set/get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        super().update(width = value, height = value)
    
    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a  == 0:
                    self.id = arg
                if a == 1:
                    self.size = arg
                if a == 2:
                    self.x = arg
                if a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            if 'size' in kwargs:
                self.size = kwargs['size']
            super().update(**kwargs)
    
    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
    