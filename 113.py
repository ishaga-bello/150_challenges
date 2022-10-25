# Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add
# that many. After all the data has been added, ask for an author and display all the books in the list by that author.
# If there are no books by that author in the list, display a suitable message.

from csv import *

add = int(input('How many records do you want to add: '))
for i in range(0,add):
    file = open ('Books.csv', 'a')
    name = input('Enter book name: ')
    age =input('Enter author: ')
    star = input('Enter year released: ')
    newRec = name + ',' + age + ',' + star +'\n'
    file.write(str(newRec))
    file.close
    
file = open('Books.csv', 'r')
author = input('Enter author name to search: ')
reader = reader(file)
for row in file:
    if author in str(row):
        print(row)
file.close