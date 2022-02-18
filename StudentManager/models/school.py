class school:
    def __init__(self, name, address, phone, country):
        self.name = name
        self.address = address
        self.phone = phone
        self.country = country

    def show(self):
        print("Tên trường: ",self.name)
        print("Địa chỉ: ",self.address)
        print("Số điện thoại: ",self.phone)
        print("Tỉnh thành: ",self.country)
