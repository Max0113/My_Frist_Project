import turtle 
import random


wind = turtle.Screen()
wind.title("younes")
wind.bgcolor("black")
wind.setup(width=800 , height=600)
wind.tracer(0)

modules_1 = turtle.Turtle()
modules_1.speed(0)
modules_1.shape("square")
modules_1.color("blue")
modules_1.shapesize(stretch_wid=1 , stretch_len=1)
modules_1.penup()
modules_1.goto(-350,0)

modules_2 = turtle.Turtle()
modules_2.speed(0)
modules_2.shape("square")
modules_2.color("red")
modules_2.shapesize(stretch_wid=1 , stretch_len=1)
modules_2.penup()
modules_2.goto(-350,150)

modules_3 = turtle.Turtle()
modules_3.speed(0)
modules_3.shape("square")
modules_3.color("yellow")
modules_3.shapesize(stretch_wid=1 , stretch_len=1)
modules_3.penup()
modules_3.goto(-350,-150)

fin = turtle.Turtle()
fin.speed(0)
fin.shape("square")
fin.color("black")
fin.shapesize(stretch_wid=100 , stretch_len=1)
fin.penup()
fin.goto(350, 0)

def new_modules_1() :
    x = modules_1.xcor()
    x += 10
    modules_1.setx(x)

def new_modules_2() :
    x = modules_2.xcor()
    x += 10
    modules_2.setx(x)

def new_modules_3() :
    x = modules_3.xcor()
    x += 10
    modules_3.setx(x)

wind.listen()
wind.onkeypress(new_modules_1, "w")
wind.onkeypress(new_modules_2, "s")
wind.onkeypress(new_modules_3, "x")


while True : 
    wind.update()
    if modules_1.xcor() > 350 and modules_1.xcor() < 340 :
        wind.clear()
        print("red he is win")
        quit()

    
