import turtle
t = turtle.Turtle()


def nhapSo():
    while True:
        try:
            num = int(input("Nhập độ dài hình vuông: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num


def vehinhvuong(a):
    count = 0
    while count < 4:
        t.forward(a)
        t.right(90)
        count += 1


if __name__ == "__main__":
    a = nhapSo()
    vehinhvuong(a)
    turtle.done()
