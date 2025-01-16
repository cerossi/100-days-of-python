from turtle import Turtle, Screen

import random

turtle = Turtle()

turtle.shape("turtle")
turtle.speed("fastest")
turtle.pensize(15)

colors = [
    "red2",
    "dark orange",
    "gold",
    "green4",
    "dodger blue",
    "purple2",
    "magenta3",
]

angles = [
    0,
    90,
    180,
    270,
]

for i in range(2000):
    turtle.color(random.choice(colors))
    turtle.forward(30)
    turtle.setheading(random.choice(angles))
    # turtle.right(random.choice(angles))

screen = Screen()
screen.exitonclick()