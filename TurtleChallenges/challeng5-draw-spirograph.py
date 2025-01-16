from turtle import Turtle, Screen

import random

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.speed("fastest")

screen.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color

for i in range(0, 360, 5):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(i)
    # turtle.right(random.choice(angles))

screen.exitonclick()