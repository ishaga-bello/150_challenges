# Using program 100, ask the user for a name and a region. Display the relevant data. Ask
# the user for the name and region of data they want to change and allow them to make
# the alteration to the sales figure. Display the sales for all regions for the name they
# choose.

sales = {'John':{'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612}, 'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859}, 'Fionna': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}
print(sales)

name = input('Enter name: ')
region = input('Enter egion(N S E W): ').upper()
decision = input('Do you want to edit the sales(y/n): ')
if decision == 'y':
    value = int(input('enter number: '))
    sales[name][region] = value
print(sales[name])