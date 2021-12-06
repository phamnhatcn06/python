import turtle  # graphic library
import math     # Math library
# Defined Variable
penDraw = turtle.Turtle()
penDraw.speed(10)
penDraw.pensize(3)  # kích cỡ

# create a Screen Object
screen = turtle.Screen()

# Screen configuration
screen.setup(1000, 1000)

# Set screen background
screen.bgcolor("#BFEFFF")
# Draw square or rectangle

# Hàm đặt vị trí con trỏ


def setPosition(longPos, latPos):
    penDraw.up()
    penDraw.goto(longPos, latPos)
    penDraw.down()

# Hàm vẽ đường thẳng


def drawLine(width, colorLine, borderWidth):
    penDraw.pensize(borderWidth)
    penDraw.pencolor(colorLine)
    penDraw.forward(width)

# Hàm vẽ hình vuông, hình chữ nhật


def drawSquare(width, height, colorBack, borderWidth):
    penDraw.pensize(borderWidth)
    penDraw.pendown()  # tạo con trỏ
    penDraw.color(colorBack)
    penDraw.pencolor("black")
    penDraw.begin_fill()
    for counter in range(1, 3):  # đây là một vòng lặp (loop)
        penDraw.forward(width)
        penDraw.right(90)
        penDraw.forward(height)
        penDraw.right(90)
    penDraw.end_fill()
    penDraw.penup()

# Hàm vẽ hình tam giác


def drawTriangle(type, width, colorBack, borderWidth, penColor="black"):
    penDraw.pendown()  # tạo con trỏ
    penDraw.color(colorBack)
    penDraw.pencolor(penColor)
    penDraw.pensize(borderWidth)
    if type == "deu":
        penDraw.begin_fill()
        for i in range(0, 3):
            penDraw.left(120)
            penDraw.forward(width)
        penDraw.end_fill()
    elif type == "vuongcan":
        penDraw.begin_fill()
        b = math.sqrt(2*math.pow(width, 2))
        # b = math.sqrt(pow(width/2, 2) + pow(height, 2)) # công thức: căn 2 (1/2 canh day) bình phuong + chieu cao binh phuong
        penDraw.forward(width)
        penDraw.left(135)
        penDraw.forward(b)
        penDraw.left(90)
        penDraw.forward(b)
        penDraw.left(135)
        penDraw.forward(b)
        penDraw.end_fill()

# Hàm vẽ hình tròn


def drawCircle(radius, borderWidth, colorBack, penColor="black"):
    penDraw.pendown()  # tạo con trỏ
    penDraw.color(colorBack)
    penDraw.pencolor(penColor)
    penDraw.pensize(borderWidth)
    penDraw.circle(radius)

# Hàm vẽ hình thang vuông


def drawSquareTrapezoid(bottom, angle, height, borderWidth, colorBack, penColor="black"):
    penDraw.pendown()  # tạo con trỏ
    penDraw.color(colorBack)
    penDraw.pencolor(penColor)
    penDraw.pensize(borderWidth)
    slope = height / math.sin(math.radians(angle))
    top = bottom - (math.cos(math.radians(angle)) * slope)
    penDraw.begin_fill()
    penDraw.forward(bottom)
    penDraw.left(180 - angle)
    penDraw.forward(slope)
    penDraw.left(angle)
    penDraw.forward(top)
    penDraw.left(90)
    penDraw.forward(height)
    penDraw.left(90)
    penDraw.end_fill()

# Hàm vẽ ngôi sao


def drawStar(size, borderWidth, colorBack, penColor="black"):
    penDraw.pendown()  # tạo con trỏ
    penDraw.color(colorBack)
    penDraw.pencolor(penColor)
    penDraw.pensize(borderWidth)
    angle = 120
    # form star
    penDraw.begin_fill()
    for side in range(5):
        penDraw.forward(size)
        penDraw.right(angle)
        penDraw.forward(size)
        penDraw.right(72 - angle)
    penDraw.end_fill()


if __name__ == "__main__":
    # Nền nhà
    setPosition(-500, -200)
    drawLine(1000, "brown", 3)
    # Nhà chính
    setPosition(-300, -200)
    drawSquare(300, -180, 'yellow', 3)
    # Mái nhà
    for i in range(0, 5):
        setPosition(-150, -20+40*i)
        drawTriangle("vuongcan", 200 - 40*i, "#8B0000", 3)
    # Ống khói
    penDraw.right(90)
    setPosition(-282, 150)
    drawSquareTrapezoid(100, 45, 50, 3, "yellow")
    setPosition(-287, 150)
    drawSquare(-20, -60, "brown", 3)
    # Cửa chính
    penDraw.left(90)
    setPosition(-190, -200)
    drawSquare(80, -120, 'green', 3)
    # Núm cửa
    setPosition(-120, -140)
    drawCircle(3, 3, "white")
    # Cửa sổ 1
    setPosition(-250, -110)
    drawSquare(20, -30, '#00BFFF', 3)
    drawSquare(20, 30, '#00BFFF', 3)
    drawSquare(-20, 30, '#00BFFF', 3)
    drawSquare(-20, -30, '#00BFFF', 3)
    # Cửa sổ 2
    setPosition(-50, -110)
    drawSquare(20, -30, '#00BFFF', 3)
    drawSquare(20, 30, '#00BFFF', 3)
    drawSquare(-20, 30, '#00BFFF', 3)
    drawSquare(-20, -30, '#00BFFF', 3)

    # Thân cây
    setPosition(200, -200)
    drawSquare(20, -100, '#8B7E66', 3)
    # Lá cây
    for j in range(0, 5):
        setPosition(210, -100+50*j)
        drawTriangle("vuongcan", 150 - 20*j, "green", 3)
    # Ngôi sao
    setPosition(220, 200)
    penDraw.right(10)
    drawStar(20, 3, "yellow")
    #  Ánh sáng 1
    penDraw.left(55)
    setPosition(230, 210)
    drawLine(60, "yellow", 3)
    #  Anh sang 2
    penDraw.left(90)
    setPosition(190, 210)
    drawLine(50, "yellow", 3)

    #  Anh sang 3
    penDraw.left(80)
    setPosition(190, 175)
    drawLine(60, "yellow", 3)
    #  Anh sang 4
    penDraw.left(115)
    setPosition(235, 175)
    drawLine(70, "yellow", 3)
    # Ve hang rao:
    penDraw.left(30)
    setPosition(60, -200)
    for k in range(1, 10):
        drawSquare(10, -80, "brown", 3)
        penDraw.up()
        setPosition(60 + 40*k, -200)
        penDraw.down()
    setPosition(60, -170)
    drawSquare(330, -10, "brown", 3)

    # Viet chu:
    setPosition(-200, -260)
    penDraw.color('deep pink')
    penDraw.write("MERRY CHRISTMAS 2021", font=("Arial", 40, "bold"))
    turtle.done()
