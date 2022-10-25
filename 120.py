from random import *

def check(num1, num2):  
    if num1 == num2:
        print('Well done answer is:')
    else:
        print('Failed my answer was:')
    print(num2)

def addition():
    num1 = randint(25,50)
    num2 = randint(1,25)
    qst = num1 - num2
    ans = int(input('%d + %d = ' %(num1, num2)))
    check(ans,qst)

def substract():
    num1 = randint(5,20)
    num2 = randint(5,20)
    qst = num1 - num2
    ans = int(input('%d - %d = ' %(num1, num2)))
    check(ans,qst)

def main():
    print('1) Addition')
    print('2) Substraction')
    state = False
    while state == False:
        selection = int(input('Select 1 or 2: '))
        if selection == 1:
            state = True
            addition()
        elif selection == 2:
            state = True
            substract()
        else:
            selection = int(input('Select 1 or 2: '))

main()