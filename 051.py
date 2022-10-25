# Using the song “10 green bottles”, display the lines “There are [num] green bottles
# hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
# should accidentally fall”. Then ask the question “how many green bottles will be
# hanging on the wall?” If the user answers correctly, display the message “There will be
# [num] green bottles hanging on the wall”. If they answer incorrectly, display the
# message “No, try again” until they get it right. When the number of green bottles gets
# down to 0, display the message “There are no more green bottles hanging on the wall”.

num = 10
qst = 'how many green bottles will be hanging on the wall?'

while num > 1:
    print('There are ', num, 'green bottles hanging on the wall, ', num, ' green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
    num -= 1
    guess = int(input(qst))
    if guess == num:
        print('There will be ', num, ' green bottles hanging on the wall')
    else:
        while guess != num:
            print('No, try again')
print('There are no more green bottles hanging on the wall')