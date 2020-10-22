# no docstrings needed for __eq__ and __repr__
import turtle

def euclid_distance (point1, point2) -> float:
""" computes Euclidean distance
Arguments:
    a (Point): a point
    b (point): another point
Returns:
    float: the euclidean distance between the points
"""
    result = return ((a.x - b.x)**2) + (a.y - b.y)**2)**0.5
    round(result)

def overlap (circle1, circle2) -> bool:
""" determine if two circles touch/overlap each other
Arguments:
    circle1 (Circle): Circle 1 center point
    circle2 (Circle): Circle 2 center point
Returns:
    bool: True if circles overlap, False if they do not
"""
    return euclid_distance(circle1.center, circle2.center) <= \
        (circle1.r + circle2.r)

if __name__ == '__main__':
    tortoise = turtle.Turtle()

def draw_circle (tortoise, circle) -> None:
""" draws a circle using turtle module
Arguments:
    turtle (Turtle): draw circle
    circle (Circle): import data to draw circle
"""
    tortoise.penup()
    tortoise.setx(x)
    tortoise.sety(y)
    tortoise.pendown()
    tortoise.circle(radius)
    turtle.done()
