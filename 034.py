# If the user enters 1, then it should ask them forthe length of one of its sides and display the
# area. If they select 2, it should ask for the baseand height of the triangle and display the area. If
# they type in anything else, it should give them a suitable error message.


print('1) Square')
print('2) Traingle')
selection = int(input('Enter a numer: '))
area = 0
if selection == 1:
    lenght = int(input('Enter a lenght of a side: '))
    area = lenght ** 2
    print(float(area))
elif selection == 2:
    base = int(input('Enter a base:'))
    height = int(input('Enter a height: '))
    area = (base * height) / 2
    print(float(area))
else:
    print('Error: Please enter a suitable number')
