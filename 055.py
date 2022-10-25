# Randomly choose a number between 1 and 5. Ask the user to pick a
# number. If they guess correctly, display the message “Well done”,
# otherwise tell them if they are too high or too low and ask them to pick a
# second number. If they guess correctly on their second guess, display
# “Correct”, otherwise display “You lose”.ls.

import random

choice = random.randint(1,5)
guess = int(input('Choose a number between 1 and 5: '))

if choice == guess:
    print('Well done')
else:
    i = 1
    while i < 2:
        if guess > choice :
            print("too high")
            guess = int(input('Try again: '))
            i += 1
            if choice == guess:
                print('correct')
            else:
                print('You lose')
        else:
            print("too low")
            guess = int(input('Try again: '))
            i += 1
            if choice == guess:
                print('correct')
            else:
                print('You lose')