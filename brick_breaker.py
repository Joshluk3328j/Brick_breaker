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
pen.goto(0, 210)
pen.color('white')
pen.write('_________________________________________________________________________________',
          align='center', font=("Helvetica", "16"))

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


# background pic
# bg = turtle.bgpic('bg.png')

# make bricks
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


make_bricks()

# wn.listen()
# wn.onclick(board.goto)
angle = random.randint(30, 90)  # current place of work so resume here
# board.getscreen()._root.mainloop()
# print("hi")

while True:
    wn.update()
    # for head going ouside boundary
    ball.onclick(ball.left(angle))
    ball.forward(10000)
    if ball.xcor() > 250 or ball.xcor() < -250 or ball.ycor() > 250 or ball.ycor() < -250:
        ball.left(-360, 360)
        ball.forward(10000)

wn.mainloop()

turtle.done()
