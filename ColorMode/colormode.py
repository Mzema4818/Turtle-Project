#Importing
from myPolygon import *
import turtle

#colors
turtle.colormode(255)
turtle.bgcolor("white")

#turtles
joe = turtle.Turtle()
bob = turtle.Turtle()
bob.speed(0)

#project
for times in range(1):
    design1(bob)
    bob.penup()
    bob.goto(550,0)
    bob.right(45)
    bob.left(90)
    bob.forward(50)
    bob.right(90)
    bob.pendown()
    design1(bob)
    bob.penup()
    bob.goto(-550,-50)
    bob.right(45)
    bob.left(90)
    bob.right(90)
    bob.pendown()
    design1(bob)
    #up= first 3
    bob.penup()
    bob.goto(325,-550)
    bob.right(45)
    bob.pendown()
    design1(bob)
    bob.penup()
    bob.goto(-225,-550)
    bob.pendown()
    design1(bob)
    #up= bottom 2
    bob.penup()
    bob.goto(-250,550)
    bob.pendown()
    design1(bob)
    bob.penup()
    bob.goto(330,500)
    bob.pendown()
    design1(bob)
    #up= top 2
