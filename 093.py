# Ask the user to enter five numbers. Sort them into order and present them to the user.
# Ask them to select one of the numbers. Remove it from the original array and save it in a
# new array.

from array import *
from random import *

num1 = array('i', [])
num2 = array('i', [])
for i in range(0,5):
    num1.append(int(input('Enter value: ')))
num1 = sorted(num1)
print(num1)

num = int(input('Select a number: '))
if num in num1:
    num1.remove(num)
    num2.append(num)
    print(num1)
    print(num2)
else:
    print('Your value is not in the array')   
