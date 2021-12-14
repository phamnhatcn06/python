import turtle  # graphic library

# create a Screen Object
screen = turtle.Screen()

# Screen configuration
screen.setup(400, 400)

# Set screen background
screen.bgcolor("#BFEFFF")
# Draw square or rectangle


def nhapSo():
    while True:
        try:
            num = int(input("NHẬP LỰA CHỌN CỦA BẠN: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num


if __name__ == "__main__":
    print("======== DANH SÁCH LỰA CHỌN HÌNH KHỐI========")
    print("1. HÌNH TRÒN")
    print("==========================")
    print("2. HÌNH VUÔNG")
    print("==========================")
    luaChonHinh = nhapSo()
    print("======== DANH SÁCH LỰA CHỌN MÀU SẮC========")
    print("1. VÀNG")
    print("==========================")
    print("2. XANH")
    print("==========================")
    print("3. ĐỎ")
    print("==========================")
    luaChonMau = nhapSo()

    hinh = 'circle' if luaChonHinh == 1 else 'square' if luaChonHinh == 2 else 9
    mau = 'yellow' if luaChonMau == 1 else 'blue' if luaChonMau == 2 else 'red' if luaChonMau == 3 else 9
    if(hinh != 9 and mau != 9):
        displayShape = turtle.Turtle()
        displayShape.shape(hinh)
        displayShape.color(mau)
        turtle.done()
    else:
        print("Du lieu nhap vao khong dung")
