
def nhapSo():
    while True:
        try:
            num = int(input("Nhap du lieu: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num


def _vetamGiacSao(soSao):
    while True:
        if(soSao == 0):
            break
        else:
            print('* '*soSao)
            soSao -= 1


def greet(name, counter):

    return f"Hi, {name}!", counter+1


if __name__ == "__main__":
    soSao = nhapSo()
    counter = 0
    name,counter = greet('Bob',counter)
    print(f"{name}!\n Counter is {counter}")
    _vetamGiacSao(soSao)
