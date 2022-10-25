# Randomly pick a whole number between 1 and 10. Ask the user to enter a number and
# keep entering numbers until they enter the number that was randomly picked.

import random

choice = random.randint(1,10)
guess = int(input('Choose a number between 1 and 10: '))

if choice == guess:
    print('Well done')
else:
    while guess != choice:
        guess = int(input('Try again: '))