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

# boundary
pen2 = turtle.Turtle()
pen2.color('white')
pen2.penup()

segments = []


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
score = 0
# High_score = 0

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write('Score: 0  High score: 0', align='center', font=("Helvetica", "16"))


# board
board = turtle.Turtle()
board.speed(0)
board.penup()
b_y = -270
board.goto(0, b_y)
wn.addshape('board.gif')
board.shape('board.gif')


def make_bricks():
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
        segments.append(brick)
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
        segments.append(brick)
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
        segments.append(brick)
        x -= 30
        if x == -300:
            break


make_bricks()

# ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(board.xcor(), board.ycor()+20)
ball.direction = "stop"


def move_right():
    x = board.xcor()
    x += 25
    if board.xcor() > -290 and board.xcor() < 265:
        board.goto(x, b_y)


def move_left():
    x = board.xcor()
    x -= 25
    if board.xcor() > -241 and board.xcor() < 310:
        board.goto(x, b_y)


angle = random.randint(30, 90)
ball.left(angle)
while True:
    ball.forward(5)
    wn.listen()
    wn.onkeypress(move_right, "d")
    wn.onkeypress(move_left, "a")
    angle = 120
    b_y = board.ycor()
    b_x = board.xcor()
    ball_y = ball.ycor()
    ball_x = ball.xcor()
    while ball.xcor() > -280 and ball.xcor() < 310 and ball.ycor() < 200:
        # this represents the boundary
        wn.update()
        ball.forward(5)
        if ball.distance(board) < 20:
            ball.left(angle)
            ball.forward(100)
        else:
            for i in segments:
                if ball.distance(i) < 20:
                    i.hideturtle()
                    ball.left(angle)
                    ball.forward(20)
                    score += 20
                    pen.clear()
                    pen.write(f'Score: {score}  High score: 0',
                              align='center', font=("Helvetica", "16"))
    if ball.ycor() <= -280:
        pen.goto(0, 0)
        pen.write('Game Over', align='center', font=("Helvetica", "16"))
        ball.hideturtle
        time.sleep(1)
        pen.clear()
        ball.goto(board.xcor(), board.ycor()+20)
        pen.goto(0, 230)
        score = 0
        pen.write('Score: 0  High score: 0',
                  align='center', font=("Helvetica", "16"))
        ball.showturtle
        ball.left(angle)
        ball.forward(7)
    else:
        # this makes the ball bounce at the boundary
        ball.left(angle)
        ball.forward(7)
        while ball.xcor() > -280 and ball.xcor() < 310 and ball.ycor() > -280 and ball.ycor() < 200:
            wn.update()
            ball.forward(7)

wn.mainloop()

turtle.done()
