# Create an array of five numbers between 10 and 100 which each have two decimal places. Ask the user to
# enter a whole number between 2 and 5. If they enter something outside of that range, display a suitable error message
# and ask them to try again until they enter a valid amount. Divide each of the numbers in the array by the number the
# user entered and display the answers shown to two decimal places.

from array import *
from random import *

num1 = array('f', [14.23, 53.25, 52.62, 11.84, 65.38])
num2 = array('f', [])
num = int(input('enter number between 2 and 5: '))
state = False
while state == False:
    if (num >= 2 and num <=5):
        state = True
    else:
        num =int(input('Try again between 2 and 5: ')) 

for i in num1:
    value = i / num
    num2.append(value)


for i in num2:
    print('%.2f'%i)