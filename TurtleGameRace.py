from turtle import Turtle, Screen
import random

moving = True
screen = Screen()
screen.setup(width = 500, height = 500)
userbet = screen.textinput(title = "Make your bet", prompt = "Pick the winning turtle's color by typing red, orange, yellow, green, blue, or purple:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = [Turtle() for i in range(len(colors))]

stringText = ""
currY = -100

winners =[]

removedTurtles = []

for i in range(len(turtles)):
    turtles[i].color(colors[i])
    turtles[i].shape("turtle")
    turtles[i].penup()
    turtles[i].goto(-230, currY)
    currY+=50

while moving:
    for i in range(len(turtles)):
        if turtles[i] not in removedTurtles:
            turtles[i].forward(random.randint(1, 10))
        if int(turtles[i].xcor()) >= 250:
            winners.append(turtles[i].color())
            print(winners)
            turtles[i].goto(230, turtles[i].ycor())
            removedTurtles.append(turtles[i])
    if len(list(set(winners)))==6:
        moving = False


if userbet in winners[0]:
    stringText+="Your turtle won! \n"
else:
    stringText+=f"Your turtle did not win! The {winners[0][0]} turtle won. \n\n"
    
for i in range(6):
    stringText+=f"{i+1}: {winners[i][0]} turtle\n"

stringText+="\nType anything or click 'OK' to exit the game \n"
final = screen.textinput(title = "Final Results", prompt = stringText)

screen.exitonclick()
