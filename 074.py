# Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number
# between 5 and 9. Display the list for those colours between the start and end numbers the user input.

color_list = ('green', 'red', 'yellow', 'pink', 'black', 'brown', 'grey', 'orange', 'blue', 'violet')
print(color_list)

sIndex = int(input('starting number between 0 and 4: '))
eIndex = int(input('end number between 5 and 9: '))

print(color_list[sIndex:eIndex])