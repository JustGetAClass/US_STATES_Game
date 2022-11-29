import turtle
import pandas
from map import Map

screen = turtle.Screen()
screen.title("U.S.A States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(725, 491)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

score = 0
guess = []

while score < 50:
    state_answer = screen.textinput(title=f"Score:{score}/50", prompt="Can you Guess all the 50 states?").title()
    if state_answer == "Exit":
        # states to learn (not guessed)
        states_to_learn = []
        for state in states:
            if state not in guess:
                states_to_learn.append(state)
                new_data = pandas.DataFrame(states_to_learn)
                new_data.to_csv("states_to_learn.csv")

        break

    if state_answer in states:
        if state_answer not in guess:
            x = int((data[data.state == state_answer]).x)
            y = int((data[data.state == state_answer]).y)
            map_state = Map(x=x, y=y, state=state_answer, num=0)
            score += 1
            guess.append(state_answer)

        elif state_answer in guess:
            map_state = Map(x=0, y=0, state=state_answer, num=1)

    elif state_answer not in states:
        map_state = Map(x=0, y=0, state=state_answer, num=2)
