from turtle import Screen, Turtle
import time
import random
import pyautogui
import serial, json
# from communitysdk import list_connected_devices, MotionSensorKit

# devices = list_connected_devices()
# msk_filter = filter(lambda device: isinstance(device, MotionSensorKit), devices)
# msk = next(msk_filter, None) # Get first Motion Sensor Kit

# def on_gesture(gestureValue):
#     return gestureValue
    
# try:
#     msk.set_mode('gesture')
# except Exception as e:
#     print(e)
    
# msk.on_gesture = on_gesture

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("orange")
screen.title("Snake Game")
isinit = True

turtles = []

ending = 275
end = False
snakelen = 5
doneEditing = False
fiid = []
x = 0
y = 0
score = 0

numFood = 1

for i in range(snakelen):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("square")
    turtle.color("white")
    turtles.append(turtle)

for turtle in turtles:
    turtle.setx(x)
    x+=30
isinit = False

def left():
    isinit = True
    turtles[0].setheading(180)
    isinit = False
def right():
    isinit = True
    turtles[0].setheading(0)
    isinit = False
def up():
    isinit = True
    turtles[0].setheading(90)
    isinit = False
def down():
    isinit = True
    turtles[0].setheading(270)
    isinit = False

def move(forwardMov):
    for i in range(len(turtles)-1, 0, -1):
        isinit = True
        newx = turtles[i-1].xcor()
        newy = turtles[i-1].ycor()
        turtles[i].goto(newx, newy)
    turtles[0].forward(forwardMov)
    isinit = False
def food():
    turtle = Turtle()
    turtle.penup()
    turtle.shape("circle")
    turtle.shapesize(0.3, 0.3)
    turtle.color("blue")
    turtle.setx(random.randint(-200, 200))
    turtle.sety(random.randint(-200, 200))
    return turtle

def extend():
    for i in range(2):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        turtles.append(turtle)

screen.listen()
# print(msk.on_gesture)
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(up, "w"
             )
screen.onkey(down, "s")
turtle2 = Turtle()
turtle2.color('blue')
style = ('Courier', 30, 'italic')
turtle2.write(f'Score: {score}', font=style, align='center')
turtle2.hideturtle()
fo = food()
while not end:
    screen.update()
    x5 = 20
    move(x5)
    if turtles[0].distance(fo)<15:
        fo.setx(random.randint(-200, 200))
        fo.sety(random.randint(-200, 200))
        extend()
        score+=1
        turtle2.reset()
        turtle2.color('blue')
        turtle2.write(f'Score: {score}', font=style, align='center')
        turtle2.hideturtle()
    if int(turtles[0].xcor())>=ending or int(turtles[0].ycor())>=ending or int(turtles[0].xcor())<=0-ending or int(turtles[0].ycor())<=0-ending:
            end = True
            x2 = 0
            turtles = [turtles[i] for i in range(0, 5)]
            turtle2.reset()
            turtle2.color('blue')
            turtle2.write(f'Game Over! Final Score: {score}', font=style, align='center')
            turtle2.hideturtle()
    for i in range(1, len(turtles)):
        if isinit:
            pass
        elif turtles[0].distance(turtles[i])<10:
            end = True
            x2 = 0
            turtles = [turtles[i] for i in range(0, 5)]
            turtle2.reset()
            turtle2.color('blue')
            turtle2.write(f'Game Over! Final Score: {score}', font=style, align='center')
            turtle2.hideturtle()
        

screen.exitonclick()
