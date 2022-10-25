# Ask the user to enter two numbers.Use whole number division to divide the first number 
# by the second and also work out the remainder and display the answer in a user-friendly
# way (e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”).

num1 = int(input('Enter a number: '))
num2 = int(input('Enter anther number: '))

whole = num1 // num2
rem = num1 % num2

print('%d divided by %d is %d with %d remaining' %(num1, num2, whole, rem))