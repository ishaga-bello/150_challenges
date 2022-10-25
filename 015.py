# Ask the user to enter their favourite colour. If they enter “red”, “RED” or
# “Red” display the message “I like red too”, otherwise display the message
# “I don’t like [colour], I prefer red”.

color = (input('Enter a color: '))
color = str.lower(color)

if(color == 'red'):
    print('I like red too')
else:
    print('I don’t like %s, I prefer red' %color)