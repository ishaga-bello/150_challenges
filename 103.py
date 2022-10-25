# Adapt program 102 to display the names and ages of all the people in the list but do not show their shoe size.

user = {}
for i in range(0,4):
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    shoe = int(input('Enter shoe size:' ))
    user[name] = {'Age': age,'Shoe size': shoe}

for i in user:
    print((i),user[i]['Age'])