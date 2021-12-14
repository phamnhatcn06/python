import fractions as fr
import math


def phanSo():
    print(fr.Fraction(4.5))
    # Tao phan so tu so nguyen:
    print(fr.Fraction(9))
    # Tap phan so tu toan tu co mau so
    print(fr.Fraction(2, 5))
    # tao phan so tu so thuc
    print(fr.Fraction(0.1))

    # Tao phan so tu string:
    print(fr.Fraction('0.1'))
    #  Xuat so Pi:
    print(math.pi)


def tinhDienTich():
    print("Nhập cạnh a:")
    canh1 = float(input())
    print("Nhập cạnh b:")
    canh2 = float(input())
    print("Nhập cạnh c:")
    canh3 = float(input())
    s = (canh1 + canh2 + canh3)/2
    dientich = math.sqrt(s*(s - canh1)*(s - canh2)*(s-canh3))
    print("chu vi tam giac:")
    print(s*2)
    print("dien tich tam giac:")
    print(dientich)


def tinhSvuong():
    print("Nhập cạnh a:")
    canhVuong = float(input())
    print("Dien tich hinh vuong:")
    print(math.pow(canhVuong, 2))
    print("Chu vi hinh vuong:")
    print(canhVuong*4)


def tinhSchunhat():
    print("Nhập cạnh a:")
    chieuDai = float(input())

    print("Nhập cạnh b:")
    chieuRong = float(input())
    print("Dien tich hinh chu nhat:")
    print(chieuDai*chieuRong)
    print("Chu vi hinh vuong:")
    print((chieuDai+chieuRong)*2)
def tinhSTron():
    print("Nhập ban kinh r:")
    radCir = float(input())
    print("Dien tich hinh tron:")
    print(math.pi * pow(radCir,2))
    print("Chu vi hinh tron:")
    print(2* math.pi * radCir)
if __name__ == "__main__":
    tinhSTron()
