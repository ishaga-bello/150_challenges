# Ask for the radius and the depth of a cylinder and work out the total volume (circle
# area*depth) rounded to three decimal places.

import math

PI = math.pi

radius = float(input('enter the radius : '))
depth = float(input('enter the depth of a cylinder: '))

area  = PI * (radius ** 2)
volume = area * depth

print(round(volume, 3))