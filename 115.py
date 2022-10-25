# Using the Books.csv file, display the data in the file along with the row number of each.

from csv import *
   
file = list(reader(open('Books.csv')))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    print(x,tmp[x])
    x += 1