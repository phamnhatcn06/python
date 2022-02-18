myList = ["Orange", "Apple", "Grape"]


def addItem(myTempList):
    print('ID of my list: ', id(myTempList))
    myTempList += ["Mango"]
    print(myTempList)


if __name__ == "__main__":
    print('ID of myTemList: ',id(myList))
    addItem(myList)
    print(myList)
    print(type(myList))