# Ask the user to enter a number. Keep asking until they enter a value over 5 and
# then display the message “The last number you entered stop the program.

 
number = int(input('input a number: '))
while number <= 5:
    number = int(input('input a number: '))        
print('The last number is: ', number)