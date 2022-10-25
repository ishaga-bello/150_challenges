# Draw a five-pointed star.

import turtle
import random

turtle.shape('arrow')

for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)

turtle.hideturtle()
turtle.exitonclick()