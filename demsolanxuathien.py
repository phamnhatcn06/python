def _Demkytu():
    letters = 'abcabcdefghi'
    frequences = {}
    for c in letters:
        # lặp các ký tự trong chuỗi ký tự . lấy giá trị ban đầu 0
        # ... tăng lên 1
        # ... sau đó tăng lên 2, 3
        frequences[c] = frequences.get(c, 0) + 1
    for f in frequences.items():
        print(f)


if __name__ == "__main__":
    _Demkytu()
