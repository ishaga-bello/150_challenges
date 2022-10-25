# Create an array which contains five numbers (two of which should be repeated). Display
# the whole array to the user. Ask the user to enter one of the numbers from the array and
# then display a message saying how many times that number appears in the list.

from array import *
from random import *

nums = array('i', [24, 43, 12, 24, 12, 12])
for i in nums:
    print(i)

check = int(input('Enter number to check: '))
print('%d is repeated %d time' %(check, nums.count(check)))    
