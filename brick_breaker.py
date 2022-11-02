from itertools import count
from random import random
import turtle
import time
import random

# screen
wn = turtle.Screen()
wn.screensize(500, 500)
wn.bgcolor('black')
wn.title('Brick Breaker')

# pen
pen = turtle.Turtle()
pen.color('green')
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write('Score: 0  High score: 0', align='center', font=("Helvetica", "16"))


# boundary
pen2 = turtle.Turtle()
pen2.color('white')
pen2.penup()


def drw_boundary():
    pen2.hideturtle()
    pen2.penup()
    pen2.goto(320, 320)
    pen2.pendown()
    pen2.goto(320, -290)
    pen2.goto(-290, -290)
    pen2.goto(-290, 320)
    pen2.goto(320, 320)
    pen2.goto(320, 210)
    pen2.goto(-290, 210)


drw_boundary()
# ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.direction = "stop"

# board
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("purple")
board.shapesize(1, 5)
board.penup()
board.goto(0, -250)
board.direction = "stop"


# make bricks
# def make_bricks():
x = 300
y = 190
for brick in range(20):
    brick = turtle.Turtle()
    brick.speed(0)
    brick.color('black')
    brick.shape('square')
    brick.penup()
    brick.hideturtle()
    brick.goto(x, y)
    brick.color('blue')
    brick.showturtle()
    x -= 30
    if x == -300:
        break
x = 300
y = 140
for brick in range(20):
    brick = turtle.Turtle()
    brick.speed(0)
    brick.color('black')
    brick.shape('square')
    brick.penup()
    brick.hideturtle()
    brick.goto(x, y)
    brick.color('blue')
    brick.showturtle()
    x -= 30
    if x == -300:
        break
x = 300
y = 90
for brick in range(20):
    brick = turtle.Turtle()
    brick.speed(0)
    brick.color('black')
    brick.shape('square')
    brick.penup()
    brick.hideturtle()
    brick.goto(x, y)
    brick.color('blue')
    brick.showturtle()
    x -= 30
    if x == -300:
        break


# make_bricks()

angle = random.randint(30, 90)
ball.left(angle)
while True:
    if random.randint(0, 1) == 0:
        angle = 120
    else:
        angle = 150
    if ball.xcor() > -280 and ball.xcor() < 310 and ball.ycor() > -280 and ball.ycor() < 200:  # this represents the boundary
        wn.update()
        ball.forward(5)
        if ball.distance(brick) < 20:
            ball.left(angle)
            ball.forward(7)
        # the ball will now stop at the boundary
    else:
        ball.left(angle)
        ball.forward(7)
        while ball.xcor() > -280 and ball.xcor() < 310 and ball.ycor() > -280 and ball.ycor() < 200:  # this represents the boundary
            wn.update()
            ball.forward(7)


wn.mainloop()

turtle.done()
