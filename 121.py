# Create a program that will allow the user to easily manage a list of names. You should
# display a menu that will allow them to add a name to the list, change a name in the
# list, delete a name from the list or view all the names in the list. There should also be a
# menu option to allow the user to end the program. If they select an option that is not
# relevant, then it should display a suitable message. After they have made a selection
# to either add a name, change a name, delete a name or view all the names, they
# should see the menu again without having to restart the program. The program
# should be made as easy to use as possible.

def addName():
    text = []
    text.append(input('Enter name: '))
    return text

def verify(text = []):
    if text == []:
        print('List is empty try adding a name first')
        exit()

def changeName(text = []):
    verify(text)
    index = int(input('Enter name index: ')) -1
    value = input('Enter value: ')
    text[index] = value


def deleteName(text =[]):
    verify(text)
    index = int(input('Enter name index: ')) -1
    del text[index]

def viewName(text = []):
    verify(text)
    for i in text:
        print(i)

def exit():
    print('Bye')
    quit()

def main():
    name =[]
    select = 0
    while select != 5:
        print('1) Add name to list.')
        print('2) Change a name in list.')
        print('3) Delete a name in list.')
        print('4) View names in list.')
        print('5) Quit program.')
        select = int(input('Select an option: '))
        if select == 1:
            name = addName()
        elif select == 2:
            changeName(name)
        elif select == 3:
            deleteName(name)
        elif select == 4:
            viewName(name)
        elif select == 5:
            exit()
        else:
            select = int(input('Select an option (1-5): '))

main()
