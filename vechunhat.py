import turtle
w = 200  # Chieu dai
h = 100  # Chieu rong


def rectangleDraw():
    pen = turtle.Turtle()
    pen.pensize(3)
    pen.pencolor("blue")
    pen.begin_fill
    for i in range(2):
        pen.forward(w)    # Đi thang ve chieu dai
        pen.right(90)     # Re phai 90 do
        pen.forward(h)    # Di thang ve chieu rong
        pen.right(90)     # Re phai 90 do
    pen.end_fill
    turtle.done()


def veHinhVuongCach2():
    pen = turtle.Turtle()
    pen.pensize(3)
    pen.pencolor("red")
    pen.begin_fill
    for i in range(4):
        pen.forward(w)
        pen.right(90)
    pen.end_fill
    turtle.done()


if __name__ == "__main__":
    veHinhVuongCach2()
    #rectangleDraw()
