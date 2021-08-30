from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(20)


def move_backword():
    turt.backward(20)


def move_left():
    turt.left(10)


def move_right():
    turt.right(10)

screen.listen()

screen.onkey(key="c", fun=turt.reset)
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="s", fun=move_backword)
screen.onkeypress(key="d", fun=move_right)

screen.exitonclick()