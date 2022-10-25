import turtle

turtle.shape('arrow')

turtle.color('black','yellow')
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90) 

turtle.end_fill()
turtle.exitonclick()