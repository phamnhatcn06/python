import turtle


def VeHinhChuNhat():
    from turtle import pensize
    # import turtle as hcn
    hcn = turtle.Turtle()
    hcn.fillcolor("green")
    hcn.speed(3)
    # Kich thuoc but to
    hcn.pensize(3)
    hcn.pencolor("red")
    hcn.begin_fill()
    for i in range(2):
        hcn.forward(200) # Dau - tuong ung voi t.backward.
        hcn.right(90)
        hcn.forward(200)
        hcn.right(90)
    hcn.end_fill()
    turtle.exitonclick()

# if __name__ == "__main__":
#     #ve_hinh_vuong()
VeHinhChuNhat()