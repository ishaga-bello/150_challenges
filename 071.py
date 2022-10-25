# Create a list of two sports. Ask the user what their favourite sport is and add this to the end of the list. Sort the
# list and display it.

sport_list = ['tennis', 'volley']

print(sport_list)

sport_list.append(input('Enter a your favorite sport: '))
print(sorted(sport_list))