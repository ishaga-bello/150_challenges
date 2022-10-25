# Ask the user to enter a number with lots of decimal places. Multiply
# this number by two and display the answer.

number = float(input('enter a number with lots of decimal places: '))
number *= 2
print(round(number, 2))