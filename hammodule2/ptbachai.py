import math


def nhapSo():
    while True:
        try:
            num = int(input("Nhập giá trị: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num


def pt_bac_hai(a, b, c):
    delta = math.pow(b, 2) ** - 4*a*c
    if(delta < 0):
        print('Phuong trinh vo nghiem')
    elif(delta == 0):
        print('Phuong trinh co nghiem kep x_1 = x_2 =', -b/(2*a))
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print('Phuong trinh co 2 nghiem phan biet: x1 = ' +
              str(x1) + ' va x2 =' + str(x2))


if __name__ == "__main__":
    print('Nhap he so a:')
    while True:
        try:
            a = nhapSo()
            if(a != 0):
                break
        except:
            print("He so a phai khác 0")
            continue
    print('Nhap he so b:')
    b = nhapSo()

    print('Nhap he so c:')
    c = nhapSo()

    pt_bac_hai(a, b, c)
