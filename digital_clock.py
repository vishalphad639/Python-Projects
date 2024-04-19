import time
import datetime as dt
import turtle

t = turtle.Turtle()
t1 = turtle.Turtle()
s= turtle.Screen()
s.bgcolor("white")

sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour

t1.pensize(5)
t1.color('red')
t1.penup()

t1.goto(-20, 0)
t1.pendown()

for i in range(2):
    t1.forward(260)
    t1.left(90)
    # t1.top(80)
    t1.forward(70)
    t1.left(90)

t1.hideturtle()
 
while True:
    t.hideturtle()
    t.clear()
    # display the time
    t.write(str(hr).zfill(2)
            + ":"+str(min).zfill(2)+":"
            + str(sec).zfill(2),
            font=("Arial Narrow", 50, "bold"))
    time.sleep(1)
    sec += 1

    t1.hideturtle()
 
while True:
    t.hideturtle()
    t.clear()
    # display the time
    t.write(str(hr).zfill(2)
            + ":"+str(min).zfill(2)+":"
            + str(sec).zfill(2),
            font=("Arial Narrow", 35, "bold"))
    time.sleep(1)
    sec += 1