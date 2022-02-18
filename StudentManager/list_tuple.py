if __name__ == "__main__":
    languages = ["Nhất", "Quang Anh", "C", "Java", "Android"]
    print('Số phần tử của list = ', len(languages))
    print("Phần tử thứ 2 = ", languages[1])
    print("Phần tử cuối cùng của list = ", languages[-1])
    print("Phần tử thứ 2 đến phần tử thứ 3 của list = ", languages[1:3])
    print("Các phần tử từ phần tử thứ 3 đến cuối list", languages[2:])
    print("List trước khi thay đổi = ", languages)
    languages[1] = "Javascript"
    print("List sau khi thay đổi = ", languages)
    languages[1:3] = ["Javascript", "Swift"]
    print("List sau khi thay đổi nhiều phần tử = ", languages)

    languages.append("C++")
    print("List sau khi thêm phần tử = ", languages)

    languages.insert(1, "Swift")
    print("List sau khi thêm phần tử = ", languages)

    print("List trước khi thêm phần tử = ", languages)

    languages_extend = [".NET", "React Native"]

    languages.extend(languages_extend)
    print("List sau khi mở rộng bằng extend() = ", languages)

    languages.remove("C++")
    print("List sau khi xóa bởi phương thức remove()= ", languages)

    languages.sort()
    print("List sau khi sắp xếp reverse = False = ", languages)

    del languages[1]
    print("List sau khi xóa bởi del= ", languages)

    remove_item = input('Nhập phần tử cần xoá')
    try:
        if remove_item in languages:
            print('Phần tử:' + remove_item + ' có trong list')
            languages.remove(remove_item)
            print("List sau khi xóa bởi phương thức remove()= ", languages)
    except:
        print('Phần tử nhập vào ko có trong list.')
