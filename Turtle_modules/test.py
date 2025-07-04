import turtle
import colorsys

wind = turtle.Screen()
wind.title("younes")
wind.bgcolor("black")
wind.setup(width=800 , height=600)
wind.tracer(0)

t = turtle.Turtle()
t.speed(0)
n = 70
h = 0
for i in range(360) :
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1 / n
    t.color(c)
    t.left(1)
    t.forward(1)
    for f in range(2) :
        t.left(2)
        t.circle(100)

turtle.done()
