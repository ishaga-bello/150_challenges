# Pig Latin takes the first consonant of a word,
# moves it to the end of the word and adds on an
# “ay”. If a word begins with a vowel you just add
# “way” to the end. For example, pig becomes igpay,
# banana becomes ananabay, and aadvark becomes
# aadvarkway. Create a program that will ask the
# user to enter a word and change it into Pig Latin.
# Make sure the new word is displayed in lower case

word = input('Input a word: ')
if (word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u'):
    word = word + 'way'
    print('Hello')
else:
    temp = word[0] + 'ay'
    word = word + temp
    word = word[1:]
    print('world')

print(word.lower())