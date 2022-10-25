# Create two arrays (one containing three numbers that the user enters and one containing a set of five random
# numbers). Join these two arrays together into one large array. Sort this large array and display
# it so that each number appears on a separate line.

from array import *
from random import *

num1 = array('i', [])
num2 = array('i', [])
for i in range(0,3):
    num1.append(int(input('Enter value: ')))

for i in range(0,5):
    num1.append(randint(10,50))

num1.extend(num2)
num1 = sorted(num1)
for i in num1:
    print(i)    
