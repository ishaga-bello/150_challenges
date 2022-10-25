# Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add
# it to the end of the nums list and display the list. Once they have entered three numbers, ask them if
# hey still want the last number they entered saved. If they say “no”, remove the last item from the list.
# Display the list of numbers.

nums = []

for i in range(0, 3):
    num = int(input('Enter number: '))
    nums.append(num)
    print(nums)
    decision = input ('Do you want last number you enterd to be saved(y/n): ')
    if decision == 'n':
        nums.remove(num)
    
print(nums)