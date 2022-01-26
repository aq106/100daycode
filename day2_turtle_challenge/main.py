from turtle import Turtle, Screen, goto
#from turtle import * # NOT recommended as not clear which module they would belong to in code...
import random as rd #alias import

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("green")

#square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

my_turtle.goto(-100,50)

#dashed line
for _ in range(20):
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
    my_turtle.forward(10)

my_turtle.goto(0,0)
my_turtle.clear()
#pentagon
psize = 50
for _ in range(2):
    #my_turtle.color((rd.randint(1,255),rd.randint(1,255),rd.randint(1,255)))
    my_turtle.color(rd.choice(["blue","red","grey"]))
    my_turtle.penup()
    # my_turtle.right(270)
    my_turtle.forward(10)
    # my_turtle.right(90)
    my_turtle.pendown()
    for _ in range(5):
        my_turtle.right(72)
        my_turtle.forward(psize)
    psize+=10


my_turtle.goto(0,0)
my_turtle.clear()
#bunch of shapes
angle_num = 3
psize=30
for _ in range(10):
    my_turtle.color(rd.choice(["blue","red","grey"]))
    my_turtle.goto(0,0)
    for _ in range(angle_num):
        my_turtle.right(360/angle_num)
        my_turtle.forward(psize)
    angle_num+=1
    psize+=10
    
my_turtle.goto(0,0)
my_turtle.clear()
#random walk
while(1):
    my_turtle.color(rd.choice(["green","black","blue","red","grey"]))
    my_turtle.right(rd.choice([0,90,180.270,360]))
    my_turtle.forward(20)

scr = Screen()
scr.exitonclick()

