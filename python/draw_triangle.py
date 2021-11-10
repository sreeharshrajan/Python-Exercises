import turtle
turtle.bgcolor("white")
turtle.pensize(1)

side = int(input("Enter the length of sides of the triangle(>100): "))

color = input("Specify the color name or HEX: ")

turtle.fillcolor(color)

turtle.begin_fill()

for _ in range(3):
    turtle.forward(side)
    turtle.right(-120)

turtle.end_fill()
