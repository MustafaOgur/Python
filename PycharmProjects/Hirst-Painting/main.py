# import colorgram
# colors = colorgram.extract("image.jpg", 22)
import turtle
# rgb_color = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_color.append(new_color)
# print(rgb_color)

from turtle import Turtle, Screen
import random
turtle.colormode(255)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
              (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (111, 126, 220), (72, 126, 220),
              (72, 212, 220), (208, 119, 147), (34, 4, 147)]

oscar = Turtle()
oscar.speed("fastest")

# Hide turtle
oscar.hideturtle()

# Change turtle's position
oscar.penup()
oscar.goto(-200, -200)

# First position of turtle
x = -200
y = -200

# for 10x10 size
for dot in range(10):
    for _ in range(10):
        oscar.pencolor(random.choice(color_list))
        oscar.dot(15)
        oscar.penup()
        oscar.forward(50)
    y += 50
    oscar.goto(x, y)


screen = Screen()
screen.exitonclick()
