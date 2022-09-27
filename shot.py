from turtle import Turtle

class Shots:
    def __init__(self):
        self.all_shots = []
        self.tank_shot = None

    class Shot(Turtle):
        def __init__(self, color, heading):
            super().__init__()

            self.shape("arrow")
            self.color(color)
            self.turtlesize(0.5, 2, 1)
            self.setheading(heading)
            self.penup()

    def move(self):
        if self.tank_shot is not None:
            self.tank_shot.forward(4)
        for shot in self.all_shots:
            shot.forward(3)

    def new_shot(self, x, y):
        shot = self.Shot(color="green", heading=270)
        shot.goto(x, y)
        self.all_shots.append(shot)

    def check_screen_edge(self):
        for shot in self.all_shots:
            if shot.ycor() == -400:
                shot.hideturtle()
                self.all_shots.remove(shot)

        if self.tank_shot is not None and self.tank_shot.ycor() == 400:
            self.tank_shot.hideturtle()
            self.tank_shot = None

    def new_tank_shot(self, tank):
        if self.tank_shot is None:
            self.tank_shot = self.Shot(color="black", heading=90)
            self.tank_shot.goto(tank.xcor(), tank.ycor())

    def remove_shot(self, shot):
        shot.hideturtle()
        self.all_shots.remove(shot)

    def remove_tank_shot(self):
        self.tank_shot.hideturtle()
        self.tank_shot = None

    def check_opposing_shot_collision(self):
        if self.tank_shot is not None:
            for shot in self.all_shots:
                if self.tank_shot.xcor() - 5 < shot.xcor() < self.tank_shot.xcor() + 5 and shot.distance(self.tank_shot) < 10:
                    self.remove_tank_shot()
                    self.remove_shot(shot)
                    break
