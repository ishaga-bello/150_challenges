# Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep
# repeating this until they type in a message all in uppercase.

state = False
while state == False:
    word = input('Enter aword in uppercase: ')
    if word.isupper():
        state = True
        print('Thanks')
    else:
        print('Try again')
