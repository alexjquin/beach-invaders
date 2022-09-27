import random
from turtle import Turtle

from shot import Shots
from tank import Tank

LEFT = "LEFT"
RIGHT = "RIGHT"


class Turtles:
    def __init__(self, speed):
        self.shot_frequency = 1000
        self.turtles = []
        self.direction = RIGHT
        self.speed = speed

        self.generate_turtles()

    class Turtle(Turtle):
        def __init__(self):
            super().__init__()
            self.setheading(270)
            self.shape("turtle")
            self.color("black", "green")
            self.penup()
            self.turtlesize(1.5, 1.5, 1)

    def generate_turtles(self) -> None:
        x = -270
        y = 300
        for row in range(0, 3):
            for index in range(0, 8):
                turtle = self.Turtle()
                turtle.goto(x, y)
                self.turtles.append(turtle)
                x += 45
            x = -270
            y -= 45

    def check_wall(self) -> None:
        for turtle in self.turtles:
            if self.direction == RIGHT and turtle.xcor() >= 270:
                self.direction = LEFT
                self.advance_turtles()
                break
            elif self.direction == LEFT and turtle.xcor() <= -270:
                self.direction = RIGHT
                self.advance_turtles()
                break

    def move(self) -> None:
        for turtle in self.turtles:
            x = turtle.xcor()
            y = turtle.ycor()

            if self.direction == LEFT:
                turtle.goto(x - self.speed, y)
            else:
                turtle.goto(x + self.speed, y)

    def advance_turtles(self) -> None:
        for turtle in self.turtles:
            x = turtle.xcor()
            y = turtle.ycor()

            turtle.forward(10)

    def reached_tank(self, tank: Tank) -> bool:
        for turtle in self.turtles:
            if turtle.ycor() == tank.ycor() + 20 and turtle.distance(tank) < 30:
                return True

    def shoot(self, shots: Shots) -> None:
        for turtle in self.turtles:
            if random.randrange(0, self.shot_frequency) == 0:
                shots.new_shot(turtle.xcor(), turtle.ycor())

    def check_hit(self, tank_shot: Shots.Shot):
        if tank_shot is not None:
            for turtle in self.turtles:
                if tank_shot.distance(turtle) <= 30:
                    turtle.hideturtle()
                    self.turtles.remove(turtle)
                    return True


