# coding: utf-8
import turtle
import random

kame = turtle.Turtle()

kame.shape('turtle')
kame.shapesize(2, 2, 3)

kame.home()
kame.clear()
kame.penup()
kame.fd(150)
kame.left(90)
kame.pendown()
kame.circle(200)
kame.penup()
kame.home()
kame.pendown()

while True:
    kame.left(random.randint(1, 360))
    kame.fd(15)
    if kame.distance(0, 0) > 200:
        kame.undo()
