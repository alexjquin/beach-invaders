import time
import turtle
from turtle import Screen

from scoreboard import Scoreboard
from shot import Shots
from turtles import Turtles
from tank import Tank


def new_tank_shot(event):
    shots.new_tank_shot(tank)


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

speed = 1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgpic("beach.gif")
screen.title("Beach Invaders")
screen.tracer(0)
screen.listen()

tank = Tank()
turtles = Turtles(speed)
scoreboard = Scoreboard()
shots = Shots()
tank_shot = None

canvas = turtle.getcanvas()
canvas.bind('<Motion>', tank.follow_mouse)
canvas.bind("<Button-1>", new_tank_shot)

time.sleep(0.5)

game_is_on = True
screen.update()

while game_is_on:
    time.sleep(0.001)
    screen.update()

    turtles.check_wall()
    turtles.move()

    turtles.shoot(shots)
    shots.move()

    if tank.hit(shots):
        scoreboard.lose_life()
        if scoreboard.lives == 0:
            game_is_on = False

    if turtles.check_hit(shots.tank_shot):
        shots.remove_tank_shot()
        scoreboard.turtle_hit()

    shots.check_screen_edge()
    shots.check_opposing_shot_collision()

    if turtles.reached_tank(tank):
        game_is_on = False

    turtles_left = len(turtles.turtles)
    if turtles_left == 0:
        speed += 1
        scoreboard.level_up()
        turtles = Turtles(speed)
    elif turtles_left <= 8:
        turtles.speed = speed + 2
        turtles.shot_frequency = 333
    elif turtles_left <= 16:
        turtles.speed = speed + 1
        turtles.shot_frequency = 500


scoreboard.game_over()

screen.mainloop()
