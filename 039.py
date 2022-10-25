# Ask the user to enter a number between 1 and 12 and then display the times table for
# that number.

number = int(input('nombre :'))
for i in range(1,number+1):
    print('%d * %d = ' %(number, i), number * i )