import turtle
turtle.bgcolor("black")
turtle.pensize(4)


def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.speed(0)
turtle.fillcolor("red")
turtle.color("red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()
turtle.left(120)
curve()
turtle.forward(112)
turtle.end_fill()
