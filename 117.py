# Create a simple maths quiz that will ask the user for their name and then generate two
# random questions. Store their name, the questions they were asked, their answers and
# their final score in a .csv file. Whenever the program is run it should add to the .csv file
# # and not overwrite anything.


from csv import *
from random import *  

file = open('Quiz.csv', 'a')
name = input('Enter user name: ')
for i in range(0,2):
    op1 = randint(10,50)
    op2 = randint(10,50)
    opt = choice(['+', '-', '/', '*'])
    qst = '%d %s %d = '%(op1, opt, op2)
    ans = input(qst)
    num1 = float(op1)
    num2 = float(op2)
    ans1 = float(ans)
    score = 0
    for count in range(0,3):
        if num1 + num2 == ans1 or num1 - num2 == ans1 or num1 * num2 == ans1 or num1 / num2 == ans1:
            score += 1
        else:
            score = 0
    score = str(score)
    rec = name + ',' + qst + ',' + ans + ',' + score +'\n'
    file.write(str(rec)) 
file.close