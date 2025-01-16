import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_pos = -125

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(-230, y_pos)
    y_pos += 50
    turtles.append(turtle)

is_race_on = True

while is_race_on:
    for turtle in turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"You've won! Turtle {winner_turtle} is the winner!")
            else:
                print(f"You've lost! Turtle {winner_turtle} is the winner!")

        turtle.forward(random.randint(0,10))


screen.listen()
screen.exitonclick()