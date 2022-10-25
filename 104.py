# After gathering the four names, ages and shoe sizes, ask the user to enter the name of the person they want to remove from
# the list. Delete this row from the data and display the other rows on separate lines.

user = {}
for i in range(0,4):
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    shoe = int(input('Enter shoe size:' ))
    user[name] = {'Age': age,'Shoe size': shoe}

getRid = input('Enter name to get rid of: ')
del user[getRid]
print(user)