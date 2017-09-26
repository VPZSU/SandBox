import turtle

x = 0
y = 0
a = int(input('довжина сторони:'))

turtle.bgcolor("blue")
turtle.speed(0)
turtle.pencolor('yellow')


def sofi(side, xpos, ypos):
    print(turtle.position())
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.setposition(xpos, ypos)

while a <= 300:
    a = a + 10
    x = x - 5
    y = y - 5
    sofi(a, x, y)
    print(a)

#sofi(a)


