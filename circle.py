from turtle import Turtle, Screen
import random

shape = Turtle()
shape.speed("fastest")
radius = 100
color = ["light pink", "papaya whip", "powder blue"]

for _ in range(radius):
    shape.color(random.choice(color))
    shape.circle(radius)
    shape.tilt(20)
    shape.left(4)

screen = Screen()
screen.exitonclick()