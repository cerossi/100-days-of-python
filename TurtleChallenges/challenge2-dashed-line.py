from turtle import Turtle, Screen

turtle = Turtle()

turtle.shape("turtle")
turtle.color("green")
turtle.speed("slowest")

for i in range(30):
    if i % 2 == 0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(10)

screen = Screen()
screen.exitonclick()