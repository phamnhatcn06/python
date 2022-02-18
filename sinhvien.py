def sortKey(e):
    return e['tuoi']


if __name__ == "__main__":
    students = [
        {'ten': 'Pham Van Nhat', 'tuoi': 30, 'sothich': 'nghe nhac'},
        {'ten': 'Bui Quang Anh', 'tuoi': 35, 'sothich': 'nghe nhac'},
        {'ten': 'Phan The Tien', 'tuoi': 25, 'sothich': 'choi game'},
        {'ten': 'Nguyen Quang Tien Anh', 'tuoi': 20, 'sothich': 'Hat'},
        {'ten': 'Le Nhat', 'tuoi': 18, 'sothich': 'nghe nhac'},
    ]

    print('Danh sach truoc khi sap xep:')
    print(students)
    students.sort(key=sortKey)
    print('Danh sach sau khi sap xep tu be den lon:')
    print(students)
    students.sort(reverse=True, key=sortKey)
    print('Danh sach sau khi sap xep tu lon den be:')
    print(students)
