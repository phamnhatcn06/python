def nhapSo():
    while True:
        try:
            num = int(input("Nhập giá trị: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num

def bangcuuchuong(num):
    for i in range(1,11):
        print(str(num) + ' x ' + str(i) + ' = ' + str(num * i)+'\n')

if __name__ == "__main__":
    print('Chọn bảng cửu chương hiển thị:')
    num = nhapSo()
    bangcuuchuong(num)