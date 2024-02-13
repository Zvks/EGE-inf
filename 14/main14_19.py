for x in '0123456789ABCDEFGHIJK':
    ok = True
    for y in '0123456789ABCDEFGHIJK':
        a = '12'+ y + x + '9'
        b = '36' + y + '99'
        if (int(a,21)+ int(b,21)) % 18 != 0:
            ok = False
    if ok:
        a = '125' + x + '9'
        b = '36599'
        print((int (a, 21)+int (b, 21)) // 18)
        break