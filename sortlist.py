def myFunc(e):
    return len(e)

if __name__ == "__main__":
    cars=['Ford','Mitsubishi','BMW','VM']
    print('Truoc khi sap xep')
    print(cars)
    cars.sort(key=myFunc)
    print('Sau khi sap xep')
    print(cars)