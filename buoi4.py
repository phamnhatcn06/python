import turtle
w = 50
def veHinhVuongCach1():
    pen = turtle.Turtle()
    # Cach 1: Ve tung canh
    pen.forward(w) # Đi thẳng
    pen.right(90) # Quay 90

    pen.forward(w)
    pen.right(90)

    pen.forward(w)
    pen.right(90)

    pen.forward(w)
    pen.right(90)

    turtle.done()

def veHinhVuongCach2():
    pen = turtle.Turtle()

    for i in range(4):
        pen.forward(w)    
        pen.right(90)
    turtle.done()
if __name__ == "__main__":
    veHinhVuongCach2()