# Ask for the name of somebody the user wants to invite
# to a party. After this, display the message “[name] has
# now been invited” and add 1 to the count. Then ask if
# they want to invite somebody else. Keep repeating this
# until they no longer want to invite anyone else to the
# party and then display how many people they have
# coming to the party.

 
msg = 'Do want to invite another person? (y/n)'
name = input('Enter person name: ')
print(name, ' has been invited')
count = 1
decision = input(msg)
while decision == 'y':        
    name = input('Enter person name: ')
    print(name, ' has been invited')
    count += 1
    decision = input(msg)

print(count, ' person(s) is(are) comming to the party')