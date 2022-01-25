"""Basic example of class...object...module and package...
"""
from turtle import Turtle, Screen, goto

my_turtle = Turtle()#creating a object from class:blueprint of set of attributes and methods that can represent that object...

print(my_turtle)#prints object location in memory...

scr = Screen()#Screen object from screen class...

#Attribute of object...
print(scr.canvheight)

#Methods of object...
my_turtle.shape("turtle")
my_turtle.color("green")
my_turtle.forward(100)
#my_turtle.onclick(goto)
#scr.onscreenclick(goto)
scr.exitonclick()


#pypi = python package index...pip install package = module+(every file is module)/framework? to do something with docs...

#Procedural programming can become complex...not modular and scalable as errors not contained and changes difficult to add...
#OOP = Object Oriented Solves that as seen form coffee machine procedure program vs oop one...day2 challenge? IA 

class user:
    #pass
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.following = 0
        self.followers = 0
    def follow(self, other_user):
        self.following+=1
        other_user.followers+=1
    def show(self):
        print(f"Name:{self.name}\nScore:{self.score}\nFollowers:{self.followers}\nFollowing:{self.following}")

#Creating Object From Class...object name like variable name can have cases...
#PascalCase = EachFirstLetterCpitalisedOnly , camelCase = firstLetterSmallRestPascal, Snake_Case = under_scores, Kebab-Case=hyphens
MyUser = user("aq106", 100)
MyUser.score+=1
MyUser.new_score="abc"
#print(MyUser.score,MyUser.new_score)

some_user = user("better",102)
MyUser.follow(some_user)

MyUser.show()
some_user.show()
