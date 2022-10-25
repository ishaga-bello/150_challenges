# Display an array of five numbers. Ask the user to select one of the numbers.
# Once they have selected a number, display the position of that item in the array. If they enter
# something that is not in the array, ask them to try again until they select a relevant item

from array import *
from random import *

num1 = array('i', [])
num2 = array('i', [])
state = False
for i in range(0,5):
    num1.append(randint(10,50))
num1 = sorted(num1)
print(num1)
num = int(input('Select a number: '))
state = False
while state == False:
    if num in num1:
        state = True
        print('%d is in position: %d' %(num, num1.index(num)+1))
    else:
        num = int(input('Try again: '))   
