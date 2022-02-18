import commonFunction as xl
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Volumes/Data/learnpython/StudentManager/components/')


class classOfSchool:
    def __init__(self, id='', name='', grade='', teacher=''):
        self.name = name
        self.grade = grade
        self.teacher = teacher

    def show(self):
        print("Mã lớp: ", self.id)
        print("Tên lớp: ", self.name)
        print("Khối: ", self.grade)
        print("GVCN: ", self.teacher)

    def addNewClass(self):
        self.name = input("Nhập vào tên lớp: ")
        print('Nhập khối:')
        self.grade = xl.nhapSo()
        self.teacher = input("Nhập vào tên GVCN: ")
