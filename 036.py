# Alter program 035 so that it will ask the user to enter their
# name and a number and then display their name that
# number of times.

name = input('Enter your name: ')
nbTimes = int(input('How many times do you want to repeat: '))
for i in range(1,nbTimes+1):
    print(name)