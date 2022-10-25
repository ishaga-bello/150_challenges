# Ask which direction the user wants to count (up or down). If they select up, then ask
# them for the top number and then count from 1 to that number. If they select down, ask
# them to enter a number below 20 and then count down from 20 to that number. If they
# entered something other than up or down, display the message “I don’t understand”.

direction = input('which direction to count (up or down): ')
direction = direction.lower()

if direction == 'up':
    nbTimes = int(input('Enter the top number: '))
    for i in range(1,nbTimes+1):
        print(i)
elif direction == 'down':
    number = int(input('nombre less than 50:'))
    for i in range(50, number-1, -1):
        print(i)
else:
    print('I don’t understand')