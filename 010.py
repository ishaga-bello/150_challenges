# There are 2,204 pounds in a kilogram. Ask the
# user to enter a weight in kilograms and convert it
# to pounds.
pound = 2_204

weight = int(input('Enter a weight in kilogram to convert it: '))
totalInPd = float(pound * weight)

print('%.2f Kg is equal to %.2f pounds' %(weight, totalInPd))