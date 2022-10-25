# Set a variable called total to 0. Ask the user to enter
# five numbers and after each input ask them if they
# want that number included. If they do, then add the
# number to the total. If they do not want it included,
# don’t add it to the total. After they have entered all five
# numbers, display the total.

total = 0

for i in range(1,6):
    number = int(input('Enter a number: '))
    decision = input('do you want it to be added (Y/N)?: ')
    decision = decision.lower()
    if decision == 'y':
        total += number
    else:
        total += 0

print(total)
