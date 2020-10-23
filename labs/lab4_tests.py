import lab4
from circle import Circle
from point import Point

point1 = Point(0, 0) 
point2 = Point(0, 0) 
point3 = Point(5, -2) 

cir1 = Circle(point1, 5)
cir2 = Circle(point2, 5)
cir3 = Circle(point3, 10)

# testing __eq__ points 
assert point1 == point2
assert point1 != point3
assert point2 != point3

# testing __repr__ points
assert repr(point1) == 'Point(0, 0)'
assert repr(point2) == 'Point(0, 0)'
assert repr(point3) == 'Point(5, -2)'

# testing __eq__ circlesß
assert cir1 == cir2
assert cir1 != cir3
assert cir2 != cir3

# testing __repr__ circles
assert repr(cir1) == 'Circle(Center: Point(0, 0), Radius: (5)'
assert repr(cir2) == 'Circle(Center: Point(0, 0), Radius: (5)'
assert repr(cir3) == 'Circle(Center: Point(5, -2), Radius: (10)'

# testing euclid_distance()
assert lab4.euclid_distance(point1, point2) == 0
assert lab4.euclid_distance(point1, point3) == round(29 ** 0.5)
assert lab4.euclid_distance(point2, point3) == round(29 ** 0.5)

# testing overlap()
assert lab4.overlap(cir1, cir2)
assert not lab4.overlap(cir1, cir3)
assert lab4.overlap(cir2, cir3)
