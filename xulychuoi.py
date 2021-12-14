# Nhap vao mot chuoi cach nhau boi dau ,
# Cat chuoi 
item = [x for x in input('Nhap vao 1 chuoi:').split(',')]
# Sap xep 
print('Truoc khi sap xep \r\n:')
for a in item:
    print(a)
item.sort()
print('Sau khi sap xep \r\n:')
for i in item:
    print(i)

# Xuat ra man hinh
print(','.join(item))