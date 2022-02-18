def greeting(text):
    print('Text user type:' + str(text))


person = {
    'name': 'Phạm Văn Nhất',
    'age': 30,
    'country': 'Hà Nội',
    'job': 'IT',

}


def showinfo(person):
    """[summary]

    Args:
        person ([type]): [description]
    """
    print('Xin chao ' + person['name'] + '. ')


def moreInfo(age, job): return print(
    'Tuoi: ' + str(age) + '. Nghe nghiep: ' + job)


def giaTriLonNhat(a):
    max = a[0]
    for i in range(len(a)):
        if max <= a[i]:
            max = a[i]
    return max


def giaTriNhoNhat(a):
    min = a[0]
    for i in range(len(a)):
        if min > a[i]:
            min = a[i]
    return min


def tinhGiaiThuaDeQuy(a):
    if a == 0:
        return 1
    return a * tinhGiaiThuaDeQuy(a - 1)


def tinhgiaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
