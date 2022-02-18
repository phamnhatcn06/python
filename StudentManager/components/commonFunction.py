def nhapSo():
    while True:
        try:
            num = int(input("Nhập giá trị: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num
    