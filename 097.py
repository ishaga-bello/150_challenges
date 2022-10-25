# Using the 2D list from program 096, ask the user to select a row and a column and display that value.

numberTable = [[2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0]]
for i in numberTable:
    print(i)
row = int(input('Enter row: '))
column = int(input('Enter column: '))
print(numberTable[row-1][column-1])