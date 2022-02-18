
def nhapSo():
    while True:
        try:
            num = int(input("Nhập giá trị: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num


def fizzzbuzz(start, end):
    for fizzbuzz in range(start, end):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz")
            continue
        print(fizzbuzz)


if __name__ == "__main__":
    print('Nhập vào số bắt đầu:')
    dau = nhapSo()
    print('Nhập vào số kết thúc:')
    cuoi = nhapSo()
    if(dau > cuoi):
        print('Số bắt đầu phải nhỏ hơn số kết thúc.')
    else:
        fizzzbuzz(dau, cuoi)
