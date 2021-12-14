import turtle
import math
# Defined Variable
penDraw = turtle.Turtle()
penDraw.speed(10)
penDraw.pensize(3)  # kích cỡ


def setPosition(longPos, latPos):
    penDraw.up()
    penDraw.goto(longPos, latPos)
    penDraw.down()


def drawSquare(width, height, colorBack, borderWidth):
    penDraw.pensize(borderWidth)
    penDraw.pendown()  # tạo con trỏ
    penDraw.color(colorBack)
    penDraw.pencolor("black")
    penDraw.begin_fill()
    for counter in range(1, 3):  # đây là một vòng lặp (loop)
        penDraw.forward(width)
        penDraw.right(90)
        penDraw.forward(height)
        penDraw.right(90)
    penDraw.end_fill()
    penDraw.penup()


if __name__ == '__main__':
    a = [100, 200, 300]
    for i in range(3):
        setPosition(a[i]*(i-1)+300,a[i])
        drawSquare(a[i], a[i], 'green', 3)
turtle.done()
