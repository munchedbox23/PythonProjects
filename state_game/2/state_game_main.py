import pandas
import turtle

screen = turtle.Screen()
image = "day 25 csv/2/blank_states_img.gif"
screen.title("U.S. State Game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("day 25 csv/2/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name?").title()
    if answer_states == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_states in all_states:
        guessed_states.append(answer_states)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_states]
        t.goto((int(state_data.x)),int(state_data.y))
        t.write(answer_states)

