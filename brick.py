import turtle

segments = []


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

segments[5].hideturtle()
turtle.done()
