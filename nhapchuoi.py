if __name__ == "__main__":
    count = 0
    while count < 7:
        chuoi = input('Nhập chuỗi kiểm tra:')
        if chuoi.lower() == 'python':
            print('Nhập đúng rồi.')
            break
        else:
            print('Nhập không đúng chuỗi yêu cầu lần ' + str(count+1))
            count += 1
