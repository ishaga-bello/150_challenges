from csv import *
file = open('Books.csv','w')
rec = 'Book,Author,Year Released\n'
file.write(rec)
file.close
for i in range(0,5):
    file = open ('Books.csv', 'a')
    name = input('Enter book name: ')
    age =input('Enter author: ')
    star = input('Enter year released: ')
    newRec = name + ',' + age + ',' + star +'\n'
    file.write(str(newRec))
    file.close