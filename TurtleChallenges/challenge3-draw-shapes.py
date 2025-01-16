from turtle import Turtle, Screen

import random

turtle = Turtle()

turtle.shape("turtle")
turtle.speed("slow")

angles = 3

colors = [
    "azure",
    "DarkOrchid4",
    "honeydew2",
    "sienna3",
    "MistyRose2",
    "LemonChiffon2",
    "VioletRed3",
    "turquoise4",
]

random.shuffle(colors)

for i in range(8):
    turtle.color(colors[i])
    angle_degree=360/angles
    print(f"i: {i}, color: {colors[i]}")
    for a in range(angles):
        turtle.forward(100)
        turtle.right(angle_degree)
    angles +=1

screen = Screen()
screen.exitonclick()