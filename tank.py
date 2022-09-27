import turtle
from turtle import Turtle

from shot import Shots

HORIZONTAL = -300


class Tank(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.setheading(90)
        self.penup()
        self.goto(0, HORIZONTAL)

        self.turtlesize(3, 2, 1)

    def follow_mouse(self, event) -> None:
        x = event.x - 300

        self.goto(x, HORIZONTAL)

    def shoot(self):
        pass

    def hit(self, shots: Shots):
        tank_y = self.ycor()

        for shot in shots.all_shots:
            if tank_y - 20 < shot.ycor() < tank_y + 20 and shot.distance(self) < 35:
                shot.hideturtle()
                shots.remove_shot(shot)
                return True
