# Ask for the total price of the bill, then ask how
# many diners there are. Divide the total bill by the
# number of diners and show how much each
# person must pay.

billPrice = float(input('Total price of bill please: '))
nberDinner = int(input('How many dinners are they: '))

payPP = billPrice / nberDinner

print('Each one should pay %.2f' %payPP)