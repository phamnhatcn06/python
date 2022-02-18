def xoanoc():
    import math
    import turtle
    k = float(input("nhap gia tri"))
    t = turtle.Turtle()

    t.speed(20)
    t.pensize(5)
    r = 10
    i = 0
    kc = 0
    while kc < k:
        t.circle(r+i, 45)
        curPos = t.position()
        kc = turtle.distance(curPos)
        print(kc)
        i += 1


if __name__ == "__main__":
    xoanoc()
