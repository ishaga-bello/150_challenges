# Create an array which will store a list of integers. Generate five random numbers and store them in
# the array. Display the array (showing each item on a separate line).

from array import *
from random import *

nums = array('i', [])
for i in range(0,5):
    nums.append(randint(10,50))
for i in nums:
    print(i)
