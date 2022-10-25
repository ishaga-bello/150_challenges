# Ask the user to enter the names of three people they want to invite to a party and store them in a list. After they have entered
# all three names, ask them if they want to add another. If they do, allow them to add more names until they answer “no”. When
# they answer “no”, display how many people they have invited to the party.

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

print('You have invited ', len(inviteList), 'persons')