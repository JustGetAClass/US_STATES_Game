from turtle import Turtle
import time


class Map(Turtle):
    def __init__(self, x, y, state, num):
        super().__init__()
        if num == 0:
            self.hideturtle()
            self.penup()
            self.goto(x, y)
            self.write(state)
        elif num == 1:
            self.clear()
            self.hideturtle()
            self.penup()
            self.pencolor("red")
            self.goto(x, y)
            self.write(f"You already guessed {state}", align="center", font=('Arial', 20, 'normal'))
            time.sleep(2)
            self.clear()
        elif num == 2:
            self.clear()
            self.hideturtle()
            self.penup()
            self.pencolor("red")
            self.goto(0, 0)
            self.write(f" {state} is not a state", align="center", font=('Arial', 20, 'normal'))
            time.sleep(2)
            self.clear()
