# import colorgram
#
# colors = colorgram.extract('hirst_painting.jpg', 20)
# colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
#
# print(colors)
import random
from turtle import Turtle, Screen, TNavigator


color_list = [(236, 35, 108), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45),
              (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91),
              (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]

INITIAL_X = -230.00
INITIAL_Y = -190.00
number_of_dots = 100

turtle = Turtle()
screen = Screen()

screen.colormode(255)

turtle.speed("fast")
turtle.penup()
turtle.goto(INITIAL_X, INITIAL_Y)

for dots_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))

    if dots_count % 10 == 0:
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.setx(INITIAL_X)
    else:
        turtle.forward(50)

screen.exitonclick()