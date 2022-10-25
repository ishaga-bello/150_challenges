# Ask the user to enter their first name and surname in lower
# case. Change the case to title case and join them together.
# # Display the finished result.

firstName = input("Enter your name: ")
surName = input('Enter your surname: ')

name = firstName.title() + surName.title()

print(name ,"\n")