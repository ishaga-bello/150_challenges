# Ask the user to enter an integer that is over 500. Work
# out the square root of that number and display it to two
# decimal places.

import math

number = float(input('enter a integer that is over 500: '))
number = math.sqrt(number)
print(round(number, 2))