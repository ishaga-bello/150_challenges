# Create a list of four three-digit numbers. Display the list to the user, showing each item from
# the list on a separate line. Ask the user to enter a three-digit number. If the number they
# have typed in matches one in the list, display the position of that number in the list,
# otherwise display the message “That is not in the list”.

numberList = [234,653,362,321]

for i in numberList: 
    print(i)

number =int(input('nter a 3 digits number: '))

if number in numberList:
    print('In index: ', numberList.index(number),)
else:
    print('That is not on the list')