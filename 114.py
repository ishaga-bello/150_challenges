# Using the Books.csv file, ask the user to enter a starting year and an end year. Display all books released between those two years.

from csv import *
  
stYear = int(input('Enter year: '))
edYear = int(input('Enter end year: '))
file = list(reader(open('Books.csv')))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(tmp[x][2]) >= stYear and int(tmp[x][2]) <= edYear:
        print(tmp[x])
    x += 1
file.close