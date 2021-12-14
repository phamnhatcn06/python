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


def drawCircle(radius, borderWidth, colorBack, penColor="black"):
    penDraw.pendown()  # tạo con trỏ
    penDraw.color(colorBack)
    penDraw.pencolor(penColor)
    penDraw.pensize(borderWidth)
    penDraw.begin_fill
    penDraw.circle(radius)
    penDraw.end_fill

if __name__ == '__main__':
    r = float(input('Nhập vào bán kính hình tròn r:'))
    chuvi = 2*math.pi*r
    dientich = math.pi*r**2
    drawCircle(r, 3, "red")
    setPosition(0, (-r*4)-50)
    penDraw.color('red')
    penDraw.pencolor("black")
    penDraw.write("Chu vi hinh tron la {} \r\n Dien tich la {}".format(
        chuvi, dientich), font=("Arial", 16, "bold"))
    turtle.done()
