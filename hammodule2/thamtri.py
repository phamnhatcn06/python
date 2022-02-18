def addInt(myTempInt):
    print("[addInt] myTempInt = ", myTempInt)
    print("[addInt] id of myTempInt = ", id(myTempInt))
    myTempInt += 5
    print("[addInt] myTempInt after add = ", myTempInt)
    print("[addInt] id of myTempInt after add = ", id(myTempInt))


if __name__ == "__main__":
    myInt = 45
    print('myInt:', myInt)
    print('id of myInt :', id(myInt))
    addInt(myInt)
    print('myInt', myInt)
    print('id of myInt', id(myInt))
