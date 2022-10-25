# Create a program that will allow the user to easily manage a list of names. You should
# display a menu that will allow them to add a name to the list, change a name in the
# list, delete a name from the list or view all the names in the list. There should also be a
# menu option to allow the user to end the program. If they select an option that is not
# relevant, then it should display a suitable message. After they have made a selection
# to either add a name, change a name, delete a name or view all the names, they
# should see the menu again without having to restart the program. The program
# should be made as easy to use as possible.

def addName():
    name = input('Enter name: ')
    names.append(name)
    return names

# def verify(text = []):
#     if text == []:
#         print('List is empty try adding a name first')
#         exit()

def changeName():
    num = 0
    for x in names:
        print(num, x)
        num += 1
    pos = int(input('Enter position of element to cahnge: '))
    name =input('Enter value: ')
    names[pos] = name
    return names

def deleteName():
    num = 0
    for x in names:
        print(num, x)
        num += 1
    pos = int(input('Enter position of element to delete: '))
    del names[pos]
    return names

def viewName():
    for i in names:
        print(i)
    print()

def main():
    state = True
    while state == True:
        print('1) Add name to list.')
        print('2) Change a name in list.')
        print('3) Delete a name in list.')
        print('4) View names in list.')
        print('5) Quit program.')
        select = int(input('Select an option: '))
        if select == 1:
            names = addName()
        elif select == 2:
            names = changeName()
        elif select == 3:
            names = deleteName()
        elif select == 4:
            names = viewName()
        elif select == 5:
            state = False
        else:
            select = int(input('Select an option (1-5): '))
        data = (names,state)


names = []
main()
