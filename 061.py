import turtle

turtle.shape('arrow')

turtle.color('black','yellow')
turtle.begin_fill()
for i in range(0,3):
    turtle.forward(100)
    turtle.right(120) 

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()