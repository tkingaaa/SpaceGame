import turtle
import random
import time

def fel():
    positionY = spaceship.ycor()
    positionX = spaceship.xcor()


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("bg.png")
space.addshape("sprite.gif")
space.onkey()

spaceship = turtle.Turtle()
spaceship.shape("sprite.gif")


while True:

    space.update()
    time.sleep(0.2)

