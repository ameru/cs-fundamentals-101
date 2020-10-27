# Lab 4 - Circle

from point import Point

class Circle:
    """ represents a point in 2D space
Attributes:
    Point (object): x coordinate
    radius (float): y coordinate
"""

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    """ add x and y to class Circle
    Arguments:
        x (float): x coordinate
        y (float): y coordinate
        radius: half the circumference of circle
    """

    def __repr__(self):
        return "Circle(%s, %d)" % (self.center, self.radius) #%d is a placeholder for a digit

    def __eq__(self, other):
        return isinstance(other, Circle) and\
            self.center == other.center and\
            self.radius == other.radius
