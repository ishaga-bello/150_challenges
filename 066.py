# Write the numbers as shown below,starting at the bottom of the numberone.

import turtle
import random

turtle.shape('arrow')

angle = random.randint(0,360)
nbLine = random.randint(0,10)
lgLine = random.randint(50,100)

for i in range(0,10):
    turtle.right(36)
    for i in range(0,nbLine):
        # line = random.choice(['blue','red','yellow','pink','green'])
        # turtle.color(line)
        turtle.forward(lgLine)
        turtle.right(angle)

turtle.hideturtle()
turtle.exitonclick()