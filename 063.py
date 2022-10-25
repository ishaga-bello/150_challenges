# Draw three squares in a row with a gap between each. Fill them using three different colours.

import turtle
import random

turtle.shape('arrow')

for i in range(0,3):
    color = random.choice(['green','red','yellow'])
    turtle.color('white',color)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
        
    turtle.end_fill()
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()

turtle.hideturtle()
turtle.exitonclick()