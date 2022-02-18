def myFunc2(e):
    return e['year']
#vận dụng 1: sắp xếp theo car hoặc car_name 
#vận dụng 2: 
#1/. Khai báo một danh sách học viên kiểu list dictionary 
# gồm tên, tuổi, sở thích
#2/. Sắp xếp theo tên, tuổi, sở thích sử dụng 
#hàm sort(key=_)
#Xuất kết quả ra màn hình  trước và sau khi sắp 
#xếp danh sách kiểu dic. 
if __name__ == "__main__":
    cars = [
        {'car':'Ford','year':2005}, 
        {'car':'Mitsubishi','year':2000}, 
        {'car':'BMW','year':2021}, 
        {'car':'Cardilac','year':2019}
    ]
    print('Danh sach truoc khi sap xep')
    print(cars)
    cars.sort(key=myFunc2)
    print('Danh sach sau khi sap xep')
    print(cars)