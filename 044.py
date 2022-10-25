# Ask how many people the user wants to invite to a party. If they enter a number below
# 10, ask for the names and after each name display “[name] has been invited”. If they
# enter a number which is 10 or higher, display the message “Too many people”.


number = int(input('How many people do you want to invite'))

if (number < 10):
    for i in range(1,number+1):
        name = input('Enter a name: ')
        print(name, 'has been invited')
else:
    print('Too many people')