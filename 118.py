# Define a subprogram that will ask the user to enter a number and save it as the variable
# “num”. Define another subprogram that will use “num” and count from 1 to that number.

def getNumber():
    num = int(input('Enter number: '))
    return num

def count(num):
    for i in range(0,num):
        print(i)

def main():
    num = getNumber()
    count(num)

main()