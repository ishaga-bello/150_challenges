# Using the 2D list from program 096, ask the user which row they would like displayed and display
# just that row. Ask them to enter a new value and add it to the end of the row and display the row
# again.


numberTable = [[2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0]]
for i in numberTable:
    print(i)

row = int(input('Which row do you want to display: '))-1
print(numberTable[row])
value = int(input('Enter a value to add: '))
numberTable[row].append(value)
print(numberTable[row])