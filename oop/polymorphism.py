"""
this is an example of overriding and overloading in python
"""

class Shape():
    PI = 3.1416
    length = None
    width = None


    def __init__(self):
        ...

    def area(self):
        ...

    @classmethod
    def double_pi(cls):
        return cls.PI * 2

    def triple_pi(self):
        return self.PI * 3

    @staticmethod
    def square_pi():
        return 3.1416**2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    # overloading: multiple declarations of same method, with change behaviour
    # depending arguments
    def area(self):
        return self.base * self.base / 2
    
    def area(self, side1, side2, side3):
        p = (side1 + side2 + side3) / 2
        return (p * (p - side1) * (p - side2) * (p - side3)) ** 0.

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
    
    # overriding: changing the implementation of
    # inherited method
    def area(self):
        return self.side ** 2