class hocsinh:
    #PHƯƠNG THỨC KHỞI TẠO CỦA LỚP
    def __init__(self,name,age,gender,school):
        #vừa khai báo thuộc tính name và vừa gán giá trị 
        #cho name, age, gender, school
        self.name = name
        self.age = age
        self.gender = gender
        self.school = school
    def show(self):
        print('name=',self.name)
        print('age=',self.age)
        print('gender=',self.gender)
        print('school=',self.school)
class lop: 
    def __init__(self,name,hedaotao):
        self.name = name 
        self.name = name
        self.hedaotao = hedaotao
    list = []
    list.append(hocsinh('Bao',35,1,'DaLat'))
    list.append(hocsinh('Binh',34,1,'DaLat'))
    list.append(hocsinh('Huyen',25,0,'DaLat'))
   

if __name__ == "__main__":
    lop1 = lop('PYTHON1','Tu xa')
    lop1.list