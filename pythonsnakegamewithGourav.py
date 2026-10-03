import random
import time
import turtle


delay=0.1
sc=0
hs=0


#Creating snake screen

s=turtle.Screen()
s.bgcolor("blue")
s.title("Naginnn....")
s.setup(700,600)

#creating a head

h=turtle.Turtle()
h.speed(0)
h.color("red")
h.fillcolor("black")
h.shape("square")
h.ht()
h.penup()
h.st()
h.direction="stop"

#Creating a food

f=turtle.Turtle()
f.speed(0)
f.shape("circle")
f.color("red")
f.fillcolor("black")
f.ht()
f.penup()
f.st()
f.goto(-250,160)
h.direction="stop"

#score board

sc=turtle.Turtle()
sc.speed(0)
sc.penup()
sc.goto(-300,260)
sc.write("your SC:-         ||     Highest Score:-     ")


#creating a all direction

def moveUp:
    if head.direction!="Up":
        head.direction="Down"
def Down:
    if head.direction!="Down":
        head.direction="Up"
def Right:
    if head.direction!="Left":
        head.direction="Right"

def Left:
    if head.direction!="Right":
        head.direction="Left"

def Stop:
    head.direction=="space"

#main

def move:
    if head.direction=="Up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="Down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="Right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="Left":
        x=head.xcor()
        head.setx(x-20)

#listen

s.listen()
s.onkey(move Up,"Up")
s.onkey(move Down,"Down")
s.onkey(move Left,"Left")
s.onkey(move Right,"Right")
s.onkey(move Stop,"space")

#




        




