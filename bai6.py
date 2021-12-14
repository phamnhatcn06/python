print("Cái này là một câu xuất ra màn hình")
a = 10
print("Giá trị của a là: " + str(a))
name = "Phạm Văn Nhất"
tuoi = 30
diachi = "Hà Nội"
print("Xin giới thiệu tôi tên là {}. Tôi {} tuổi, hiện đang sống tại {}".format(
    name, str(tuoi), diachi))

my_string = 'hello world'
i = 1
for x in my_string:
    print('Ký tự trong chuỗi lần lượt là: {} : {}'.format(str(i), x))
    i += 1
print("Chiều dài của chuỗi trên là {}".format(str(len(my_string))))

chuoi_1 = input('Nhập vào chuỗi 1: ')
chuoi_2 = input('Nhập vào chuỗi 2: ')
if chuoi_1 in chuoi_2:
    print('Chuỗi 1 có trong chuỗi 2')
else:
    print('Chuỗi 1 không nằm trong chuỗi 2')


# Xuat chuoi theo thư tu:
thutu = 'Xin chào tất cả mọi người'
print(thutu[2:10])

#Chuoi Hoa thuong:
string = 'My Computer Name'
print(string.upper())
print(string.lower())