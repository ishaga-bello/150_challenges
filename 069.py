# Create a tuple containing the names of five countries and display the whole tuple. Ask
# the user to enter one of the countries that have been shown to them and then display
# the index number (i.e. position in the list) of that item in the tuple.

country_list = ('cameroon', 'chad', 'congo', 'mali', 'nigeria')

print(country_list)

country = input('Enter a country in the list: ')
print(country_list.index(country) + 1)