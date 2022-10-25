# Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and display the entire file.

print('1) create a new file')
print('2) Display thefile')
print('3) Add new item to file')
select = int(input('Make a selection 1, 2, or 3: '))
state = False
while state == False:
    if select == 1:
        f = open('Subjects.txt', 'w')
        subject = input('Enter subject: ') + '\n'
        f.write(subject)
        f.close
        state = True
    elif select == 2:
        f = open('Subjects.txt', 'r')
        print(f.read())
        f.close
        state = True
    elif select == 3:
        f = open('Subjects.txt', 'a')
        subject = input('Add subject: ') + '\n'
        f.write(subject)
        f.close
        state = True
    else:
        select = int(input('Please select 1, 2, or 3: '))