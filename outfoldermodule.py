
# importing sys

import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Volumes/Data/learnpython/ham-module/')
import turtle

# import dreamhome as draw
import mymodule as md

def show():
    print(md.person['name'] + ':')
    md.greeting(input("Nhap vao chuoi hien thi:"))


def nhapSo():
    while True:
        try:
            num = int(input("Nhập giá trị: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num


if __name__ == "__main__":
    md.showinfo(md.person)
    md.moreInfo(md.person['age'], md.person['job'])
    a = []
    i = 0

    print("Nhap vao so phan tu mang A:")
    countA = nhapSo()
    print("Nhap vao danh sach mang A:")
    while i < countA:
        so = nhapSo()
        a.insert(i, so)
        i += 1
    # a = [1, 2, 4, 5, 6, 7, 8]
    max = md.giaTriLonNhat(a)
    minA = md.giaTriNhoNhat(a) 
    print('So lon nhat:' + str(max))
    print('So nho nhat:' + str(minA))
    # draw.drawSquare(20, 20, '#f00', 3)
    # turtle.done()
    print('Nhap vao so giai thua can tinh:')
    so = nhapSo()
    gt = md.tinhGiaiThuaDeQuy(so)
    print('Giai thua de quy:' + str(gt))
    gtk = md.tinhgiaithua(so)
    print('Giai thua khong de quy:' + str(gtk))
