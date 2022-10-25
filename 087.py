# Ask the user to type in a word and then display it backwards on separate lines. For
# instance, if they type in “Hello” it should display as shown below:

word = input('Enter a word: ')
for i in range(len(word),0,-1):
    print(word[i-1])