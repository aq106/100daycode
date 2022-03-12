from turtle import Turtle, Screen, circle
#from turtle import * # NOT recommended as not clear which module they would belong to in code...
import random as rd #alias import

scr = Screen()
my_turtle = Turtle()
my_turtle.shape("turtle")

def square():
    my_turtle.goto(0,0)
    my_turtle.clear()
    my_turtle.color("green")
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)


def dline():
    #dashed line
    my_turtle.goto(-100,50)
    my_turtle.clear()
    for _ in range(20):
        my_turtle.penup()
        my_turtle.forward(10)
        my_turtle.pendown()
        my_turtle.forward(10)

def pentagon():
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


def shapes():
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


def random_walk():
    my_turtle.goto(0,0)
    my_turtle.clear()
    #random walk
    my_turtle.pensize(5)
    my_turtle.speed("fastest")
    scr.colormode(255)
    while(1):
        #my_turtle.color(rd.choice(["green","black","blue","red","grey"]))
        my_turtle.pencolor((rd.randint(1,255),rd.randint(1,255),rd.randint(1,255)))
        my_turtle.setheading(rd.choice([0,90,180,270]))
        my_turtle.forward(20)

def circles():
    my_turtle.goto(0,0)
    my_turtle.clear()
    #random walk
    my_turtle.pensize(1)
    my_turtle.speed("fastest")
    scr.colormode(255)
    i=3
    while(1):
        #my_turtle.color(rd.choice(["green","black","blue","red","grey"]))
        my_turtle.pencolor((rd.randint(1,255),rd.randint(1,255),rd.randint(1,255)))
        my_turtle.right(i)
        my_turtle.circle(50)
        i+=3

def main():
    my_turtle.penup()
    my_turtle.color("green")
    my_turtle.write("Click to Exit!",font=("Calibri", 12, "bold"))
    my_turtle.goto(0,20)
    my_turtle.write("Press 'r' for random walk!",font=("Calibri", 12, "bold"))
    my_turtle.goto(0,40)
    my_turtle.write("Press 's' for shapes!",font=("Calibri", 12, "bold"))
    my_turtle.goto(0,60)
    my_turtle.write("Press 'p' for pentagons!",font=("Calibri", 12, "bold"))
    my_turtle.goto(0,80)
    my_turtle.write("Press 'q' for squares!",font=("Calibri", 12, "bold"))
    my_turtle.goto(0,100)
    my_turtle.write("Press 'c' for circles!",font=("Calibri", 12, "bold"))
    my_turtle.goto(0,160)
    my_turtle.pendown()
    scr.onkeypress(dline, "d")
    scr.onkeypress(pentagon, "p")
    scr.onkeypress(shapes, "s")
    scr.onkeypress(random_walk, "r")
    scr.onkeypress(square, "q")
    scr.onkeypress(circles, "c")
    scr.listen()
    scr.exitonclick()

if __name__ == '__main__':
    main()
