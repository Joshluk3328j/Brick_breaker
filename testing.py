import turtle
board = turtle.Turtle()
wn = turtle.Screen()
wn.addshape('board.gif')
board.shape('board.gif')
board.goto(0, 100)


def move_right():
    x = board.xcor()
    x += 30
    if board.xcor() > -250 and board.xcor() < 250:
        board.goto(x, 180)


def move_left():
    x = board.xcor()
    x -= 30
    if board.xcor() > -240 and board.xcor() < 310:
        board.goto(x, 180)


wn.listen()
wn.onkeypress(move_right, "d")
wn.onkeypress(move_left, "a")
wn.mainloop()
