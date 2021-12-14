def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(i, "Invalid day of week")
if __name__  == "__main__":
    i  = int(input("Nhap vao ngay"))
    print(week(i))
