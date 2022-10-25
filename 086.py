# Ask the user to enter a new password. Ask them to enter it again. If the two passwords
# match, display “Thank you”. If the letters are correct but in the wrong case, display the
# message “They must be in the same case”, otherwise display the message “Incorrect”.

pwd1 = input('Enter password: ')
pwd2 = input('Reenter password: ')
if pwd1 == pwd2:
    print('Thank you')
elif pwd1.islower() and pwd2.isupper():
    print('letter shoud be in same case')
else:
    print('Incorrect')