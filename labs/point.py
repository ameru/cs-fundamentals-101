# Lab 4 - Point

class Point:
""" represents a point in 2D space
Attributes:
    x (float): x coordinate
    y (float): y coordinate
"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
    """ add x and y to class Point
    Arguments:
        x (float): x coordinate
        y (float): y coordinate
    """

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y) #%d is a placeholder for a digit

    def __eq__(self, other):
        return isinstance(other, Point) and\
            self.x == other.x and\
            self.y == other.y
