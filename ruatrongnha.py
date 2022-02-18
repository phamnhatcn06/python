# Import thư viện đồ họa turtle
import turtle
# Import thư viện sinh số ngẫu nhiên
import random as r

# khởi tạo turtle
t = turtle.Turtle()
t.shape("turtle")
# Ẩn hình ảnh rùa
t.hideturtle()
t.pensize(3)
t.color("blue")
t.speed(1)
t.penup()
# Đặt vị trí ban đầu của con rùa sang bên trái
# so với vị trí giữa màn hình 400 pixel
# Mục đích để rùa chạy không ra khỏi màn hình
# khi vòng lặp quá lớn
t.goto(-400, 0)
# Hiển thị hình ảnh con rùa
t.showturtle()

count = 0
while count < 10:
    # sinh hai giá trị ngẫu nhiên
    down = r.randint(20, 50)
    up = r.randint(20, 50)
    t.pendown()
    # rùa tiến về phía trước với giá trị ngẫu
    # nhiên ở trên, có để lại nét vẽ
    t.forward(down)
    t.penup()
    # rùa tiến về phía trước với giá trị ngẫu
    # nhiên ở trên, không để lại nét vẽ
    t.forward(up)
    count += 1
turtle.done()
