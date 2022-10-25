# Create a list containing the titles of four TV programmes and display them on separate lines. Ask the
# user to enter another show and a position they want it inserted into the list. Display the list again,
# showing all five TV programmes in their new positions.

tvList = ['Friends', 'STNL', 'SNK']

for i in tvList: 
    print(i)

show = input('Enter a show name: ')
index = int(input('Enter a position'))
tvList.insert(index, show)
print(tvList)
