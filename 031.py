# Ask the user to enter the radius of a circle (measurement from the centre point to the edge).
# Work out the area of the circle (π*radius 2 ).

import math

PI = math.pi
radius = float(input('enter the radius of a circle: '))

area  = PI * (radius ** 2)

print(round(area, 5))