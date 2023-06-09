from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "purple", "black", "blue", "orange"]
all_turtles = []

color_index = 0
x = -240
y = -120

for turtle in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[color_index])
    color_index += 1
    turtle.penup()
    turtle.goto(x=x, y=y)
    y += 40
    all_turtles.append(turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
