# Randomly pick a whole number between 1 and 10. Ask the user to enter a number and
# keep entering numbers until they enter the number that was randomly picked.

import random

import random
num = random.randint(1,10)
state = False
while state == False:
    guess = int(input('enter a number: '))
    if guess == num:
        state = True
        print('Well done')
    elif guess > num:
        print('Too high')
    else:
        print('Too low')

