# Ask for two numbers. If the first one is larger than the second, display
# the second number first and then the first number, otherwise showthe first number first and
# then the second.

num1 = int(input('Enter a number: '))
num2 = int(input('Enter anther number'))

if(num2 > num1):
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)