import turtle
pen = turtle.Turtle()
w = 100
h = 100
for i in range(4):
    pen.forward(w)
    pen.right(90)
    pen.forward(h)
pen.up()
pen.goto(100, 100)
turtle.done()
