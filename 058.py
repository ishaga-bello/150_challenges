# Make a maths quiz that asks five questions by randomly
# generating two whole numbers to make the question
# (e.g. [num1] + [num2]). Ask the user to enter the
# answer. If they get it right add a point to their score. At
# the end of the quiz, tell them how many they got correct
# out of five.

import random

c = 0
i = 0
while i != 5:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    num = num1 + num2
    guess = int(input('%d + %d = ' %(num1, num2)))
    if guess == num:
        c += 1
    i += 1
print('Well done you had', c, 'on 5')


    # while guess != num:
    #     guess = int(input('%d + %d = ' %(num1, num2)))