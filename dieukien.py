def nhapSo():
    while True:
        try:
            num = int(input("Nhap du lieu: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num


def checkDoTuoi():
    namNay = 2021
    nam = nhapSo()
    if(nam < 1970 or nam > namNay):
        print("Tuổi bạn nhập không năm trong khoảng cho phép.")
    else:
        soTuoi = namNay - nam
        print("Bạn năm nay đã {} tuổi.\r\n".format(soTuoi))
        if(soTuoi == 0):
            print("Hello World Baby.")
        elif(soTuoi > 0 and soTuoi < 6):
            print("Cháu còn ở tuổi mầm non.")
        else:
            print("Em chưa 18. Cẩn thận nha anh.") if(
                soTuoi >= 6 and soTuoi < 18) else print("bạn đủ tuổi dân sự rồi.")


if __name__ == "__main__":
    checkDoTuoi()
