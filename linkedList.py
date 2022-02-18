def nhapSo():
    while True:
        try:
            num = int(input("Nhập giá trị: "))
            break
        except:
            print("Dữ liệu không phải là số.")
            continue
    return num


class Node:
    def __init__(self, dataval=None):
        # tạo một nút của dslk trỏ tới None = Null
        # Vừa khởi tạo, vừa gán giá trị cho dataval, nextval (datavalue,nextvalue)
        # next value chứa địa chỉ của nút tiếp theo
        self.dataval = dataval
        self.nextval = None


class SlinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        # Duyệt từ đầu đến cuối danh sách liên kết
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def sumNum(self):
        tong = 0
        printval = self.headval
        while printval is not None:
            tong += int(printval.dataval)
            printval = printval.nextval
        print('Tong trong list lien ket:' + str(tong))

    # chèn một phần tử vào đầu danh sách liên kết
    def AtBegining(self, newdata):
        # self = danh sách liên kết
        NewNode = Node(newdata)
        # cập nhật nút mới tới nút đã có
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtTheEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        lastNode = self.headval
        while(lastNode.nextval):
            lastNode = lastNode.nextval
        lastNode.nextval = NewNode

    def deleteNode(self, position):
        if self.headval is None:
            return
        if position == 0:
            self.headval = self.headval.next
            return self.headval
        index = 0
        current = self.headval
        prev = self.headval
        temp = self.headval
        while current is not None:
            if index == position:
                temp = current.nextval
                break
            prev = current
            current = current.nextval
            index += 1
        prev.nextval = temp
        return prev


if __name__ == "__main__":
    list1 = SlinkedList()
    list1.headval = Node(1)

    e2 = Node(2)
    e3 = Node(3)
    # Lien kết nút đầu tiên tới nút thứ hai
    list1.headval.nextval = e2
    e2.nextval = e3
    for i in range(2, 5):
        numInsert = nhapSo()
        list1.AtTheEnd(numInsert)
    print('Them phan tu dau danh sach:')
    numFirst = nhapSo()
    list1.AtBegining(numFirst)
    print('Them phan tu vao cuoi danh sach:')
    numLast = nhapSo()
    list1.AtTheEnd(numLast)
    print('Danh sach truoc khi xoa:')
    list1.listprint()
    print('Xoa phan tu thu 4:')
    list1.deleteNode(4)
    # In danh sach
    print('Danh sach sau khi xoa:')
    list1.listprint()
    # Tinh tong danh sach
    list1.sumNum()
