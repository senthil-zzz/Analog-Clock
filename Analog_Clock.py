import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.title("Analog Clock")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def sketch_clock(h, m, s, pen):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90)
    angle = (h/12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = (s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(160)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    print("The time right now in Oxford, UK is:", h,":",m,":",s)
    sketch_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)
    pen.clear()

wn.mainloop()