import turtle
from turtle import Screen, Turtle
import pandas

writer = Turtle()
screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state


def write_state_to_screen(x_cor, y_cor, state_name):
    writer.hideturtle()
    writer.penup()
    writer.goto(x=x_cor, y=y_cor)
    writer.write(arg=state_name)


guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn")
        break

    for state in all_states:
        if answer_state == state:
            if answer_state not in guessed_states:

                guessed_states.append(answer_state)

                answer_state_row = data[data.state == answer_state]
                answer_state_x_cor = int(answer_state_row.x)
                answer_state_y_cor = int(answer_state_row.y)

                write_state_to_screen(answer_state_x_cor, answer_state_y_cor, answer_state)
