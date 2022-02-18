def demchuHoa():
    s = input('Nhap chuoi cua ban:')
    d = {'UPPERCASE': 0, 'LOWERCASE': 0}
    for c in s:
        if c.isupper(): d['UPPERCASE'] += 1 
        elif c.islower(): d['LOWERCASE'] += 1 
        else: pass
    print('So ky tu hoa',d['UPPERCASE'])
    print('So ky tu thuong',d['LOWERCASE'])

if __name__ == "__main__":
    demchuHoa()
