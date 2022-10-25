from csv import *

file = open ('Books.csv', 'a')
name = input('Enter book name: ')
age =input('Enter author: ')
star = input('Enter year released: ')
newRec = name + ',' + age + ',' + star +'\n'
file.write(str(newRec))
file.close
file = open('Books.csv', 'r')
for row in file:
    print(row)
file.close