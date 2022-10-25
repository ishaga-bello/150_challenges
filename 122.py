# If the user selects 1, allow them to add to a file
# called Salaries.csv which will store their name
# and salary. If they select 2 it should display all
# records in the Salaries.csv file. If they select 3 it
# should stop the program. If they select an
# incorrect option they should see an error
# message. They should keep returning to the
# menu until they select option 3.

import csv

def addFile():
    file = open('Salaries.csv', 'a')
    name = input('Enter name: ')
    salary = input('Enter salary: ')
    rec = name + ',' + salary + '\n'
    file.write(str(rec))
    print(name, 'added')
    file.close
    print()

def viewFile():
    file = open('Salaries.csv', 'r')
    for row in file:
        print(row)
    file.close
    print()


def main():
    select = 0
    while select != 3:
        print('1) Add to file')
        print('2) View all records')
        print('3) Quit progam')
        select = int(input('Select an option: '))
        if select == 1:
            addFile()
        elif select == 2:
            viewFile()
        elif select == 3:
            quit()
        else:
            print('1) Add to file')
            print('2) View all records')
            print('3) Quit progam')
            select = int(input('Select an option: '))


main()
