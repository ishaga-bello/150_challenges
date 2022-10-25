# Ask the user to enter a number and then enter another number. Add these
# two numbers together and then ask if they want to add another number. If they
# enter “y", ask them to enter another number and keep adding numbers until they
# do not answer “y”. Once the loop has stopped, display the total.

 
number1 = int(input('input a number: ')) 
number2 = int(input('input a number: '))
total = number1 + number2
decision = input('Do want to add another number? (y/n)')
while decision == 'y':        
    number = int(input('input a number: '))
    total += number
    decision = input('Do want to add another number? (y/n)')

print('\nTotal is:', total)