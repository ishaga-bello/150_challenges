# Ask the user to type in their favourite school subject.
# Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.

subject = input('Enter favourite school subject: ')
for i in subject:
    print(i, end='-')