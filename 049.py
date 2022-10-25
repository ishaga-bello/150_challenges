# #Create a variable called compnum and set the value to 50. Ask the user to enter a
# number. While their guess is not the same as the compnum value, tell them if
# their guess is too low or too high and ask them to have another guess. If they enter
# the same value as compnum, display the message “Well done, you took [count] attempts”.

 
COMPNUM = 50
COUNT = 0
guess = int(input('Enter a value: '))
while guess != 50:
    if guess > 50:
        print('Too high')
    else:
        print('Too low')
    guess = int(input('Enter a value: '))
    COUNT += 1

print('Well done you took ', COUNT, 'attempts')