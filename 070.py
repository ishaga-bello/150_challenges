# Add to program 069 to ask the user to enter a number and display the country in that position.

country_list = ('cameroon', 'chad', 'congo', 'mali', 'nigeria')

print(country_list)

country = int(input('Enter a country number: '))
print(country_list[country-1])