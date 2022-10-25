# Ask the user to enter a number between 10 and 20. If they enter a value under 10,
# display the message “Too low” and ask them to try again. If they enter a value
# above 20, display the message “Too high” and ask them to try again. Keep repeating
# this until they enter a value that is between 10 and 20 and then display the
# message “Thank you”.

 
guess = int(input('Enter a value between 10 and 20: '))
while (guess < 10 or guess > 20):
    if guess > 20:
        print('Too high')
        guess = int(input('Try again: '))
    elif guess < 10:
        print('Too low')
        guess = int(input('Try again: '))
    print("Thank you")