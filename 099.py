# Change your previous program to ask the user which row they want displayed. Display that
# row. Ask which column in that row they want displayed and display the value that is held
# there. Ask the user if they want to change the value. If they do,ask for a new value and change
# the data. Finally, display the whole row again.

numberTable = [[2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0]]
for i in numberTable:
    print(i)

row = int(input('Which row do you want to display: '))-1
print(numberTable[row])
column = int(input('Which column fro row do you want to display: '))-1
print(numberTable[row][column])
decision = input('Do you want to change the value(y/n): ')
if decision == 'y':
    value = int(input('Enter a value to add: '))
    numberTable[row][column] = value
print(numberTable[row])