from random import *

def compNum():
    low = int(input('Entre a low number: '))
    high = int(input('Enter a high number: '))
    compnum = randint(low,high)
    return compnum

def userNum():
    print('I am thinking of a number... ')
    num = int(input('Enter number i am thinking of: '))
    return num

def compare(num, compnum):
    state = False
    while state == False:
        if num == compnum:
            print('Well done')
            state = True
        elif num < compnum:
            print('Too low')
            num = int(input('Try again: '))
        else:
            print('Too high')
            num = int(input('Try again: '))

def main():
    compChoice = compNum()
    userChoice = userNum()
    compare(userChoice, compChoice)

main()