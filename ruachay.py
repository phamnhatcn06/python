import turtle as t
import random
import time

screen = t.Screen()
screen.setup(width=800, height=400)
guess = screen.textinput(prompt='Dự đoán con rùa nào chiến thắng?', title='Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây , cam, hồng)')
colors = ['red', 'brown', 'blue', 'green', 'orange', 'pink']
x = -250
y_position = [0, -30, 30, -60, 60, 90]
turtle_speed = [10,15,20,25,30,5]
all_turtles = []
run = True
start = time.time()
for turtle in range(0,6):
        turtles = t.Turtle(shape='turtle')
        turtles.penup()
        turtles.goto(x=-250, y=y_position[turtle])
        turtles.color(colors[turtle])
        all_turtles.append(turtles)

def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.choice(turtle_speed))
        if turtle.xcor() > 250:
            run = False
            timeStop = time.time() - start
            print('Con rùa màu: ' + turtle.pencolor() + ' về đích đầu tiên.Thời gian:'+ str(timeStop))

while run:
    random_walk(all_turtles)

screen.exitonclick()