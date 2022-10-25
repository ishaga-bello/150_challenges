# Ask the user to enter their first name and then ask them to
# enter their surname. Join them together with a space between
# and display the name and the length of whole name.

firstName = input("Enter your name: ")
surName = input('Enter your surname: ')

name = firstName + ' ' + surName

print(name ,"\n")
print(len(name))