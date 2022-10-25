# Change program 076 so that once the user has completed their list of names, display the
# full list and ask them to type in one of the names on the list. Display the position of that
# name in the list. Ask the user if they still want that person to come to the party. If they
# answer “no”, delete that entry from the list and display the list again.

inviteList = []

for i in range(0,3):
    inviteList.append(input('Enter name: '))

print(inviteList)

state = True
while state == True:
    decision = input('Do you want to add more people(y/n): ')
    if decision == 'y':
        inviteList.append(input('Enter name: '))
    else:
        state = False

print(inviteList)

name = input('Enter a name to display index: ')
if name in inviteList:
    print(inviteList.index(name)+1)
    invite = input('Do you still wnat to invite %s (y/n)' %name)
    if invite == 'n':
        del inviteList[inviteList.index(name)]
    print(inviteList)
    