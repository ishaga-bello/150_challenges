# Import the data from the Books.csv file into a list. Display the list to the user. Ask them to select which row from the list
# they want to delete and remove it from the list. Ask the user which data they want to change and allow them to change it.
# Write the data back to the original .csv file, overwriting the
# existing data with the amended data.


from csv import *
   
file = list(reader(open('Books.csv')))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    print(x,tmp[x])
    x += 1

getRid = int(input('Enter a row to delete: '))
del tmp[getRid]

x = 0
for row in tmp:
    print(x,tmp[x])
    x += 1

row = int(input('Which row do you want to change value: '))
column = int(input('Which column do you want to change value: ')) - 1
value = input('Enter value to modify')
tmp[row][column] = value

file = open('Books.csv', 'w')
x = 0
for row in tmp:
    rec = tmp[x][0] + ',' + tmp[x][1] + ',' + tmp[x][2] + '\n'
    file.write(rec)
    x += 1
file.close

file = open('Books.csv' ,'r')
for row in file:
    print(row)
file.close