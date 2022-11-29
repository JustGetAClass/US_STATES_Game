from turtle import Turtle
import time


class Map(Turtle):
    def __init__(self, x, y, state, num):
        super().__init__()
        if num == 0:
            self.drawing("black", x, y)
            self.goto(x, y)
            self.write(state)
        elif num == 1:
            self.clear()
            self.drawing("red", x, y)
            self.write(f"You already guessed {state}", align="center", font=('Arial', 20, 'normal'))
            self.refresh()
        elif num == 2:
            self.clear()
            self.drawing("red", x, y)
            self.write(f" {state} is not a state", align="center", font=('Arial', 20, 'normal'))
            self.refresh()

    def drawing(self, color, x, y):
        self.hideturtle()
        self.penup()
        self.pencolor(color)
        self.goto(x, y)

    def refresh(self):
        time.sleep(2)
        self.clear()
