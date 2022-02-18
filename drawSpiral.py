import turtle

t = turtle.Turtle()

# bán kinh hinh tron
r = 10


def drawSpiral(r):
    for i in range(8):
        t.circle(r + i, 45)


if __name__ == "__main__":
    t.goto(1,1)
    drawSpiral(r)
    
    a = t.position()
    kc = turtle.distance(a) 
    print(a)
    print(kc)
    turtle.done()
