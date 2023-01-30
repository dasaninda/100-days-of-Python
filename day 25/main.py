## US State Guessing ###

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

guess_states = []
all_state = data.state.to_list()



while len(guess_states) < 50:
    answer = screen.textinput(title=f"{len(guess_states)}/50 States Guessed", prompt="Name a State").title()
   
    if answer == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guess_states:
                missing_states.append(state)          
        break

    if answer in all_state:
        if answer not in guess_states:
            guess_states.append(answer)
            state_data = data[data.state == answer]
            x_axis, y_axis = int(state_data.x), int(state_data.y)
            t.goto(x_axis, y_axis)
            t.write (answer)

