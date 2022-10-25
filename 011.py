# Task the user to enter a number over 100 and then enter a number under
# 10 and tell them how many times the smaller number goes into the larger
# number in a user-friendly format.

nbOver = int(input('Enter a number > 100: '))
nbUnder = int(input('Enter a number < 10: '))

nbTimes = (nbOver / nbUnder)

print(nbUnder, 'goes into ', nbOver, nbTimes, 'times')