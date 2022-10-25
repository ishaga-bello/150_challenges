# Ask the user to type in their name and then tell them how many vowels are in their name.

count = 0
name = input('Enter name: ')
for i in name:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count += 1

print('You have %d vowel(s)' %count)