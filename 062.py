# Draw a circle.

import turtle

turtle.shape('arrow')

turtle.color('black','yellow')
turtle.begin_fill()
for i in range(0,360):
    turtle.forward(1)
    turtle.right(1) 

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()