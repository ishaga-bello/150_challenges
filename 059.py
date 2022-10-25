# Display five colours and ask the user to pick one. If they
# pick the same as the program has chosen, say “Well
# done”, otherwise display a witty answer which involves
# the correct colour, e.g. “I bet you are GREEN with envy”
# or “You are probably feeling BLUE right now”. Ask
# them to guess again; if they have still not got it right,
# keep giving them the same clue and ask the user to
# enter a colour until they guess it correctly.

import random


color = random.choice(['green', 'yellow', 'pink', 'blue', 'red'])
print('Color: green(G) yellow(P) pink(P) blue(B) red(R): ')
state = False
while state == False:
    guess = input('Choose a color:')
    guess = guess.lower()
    if guess == color:
        print('Well done')
        state = True
    else:
        print('Ibet you are %s right now' %color)