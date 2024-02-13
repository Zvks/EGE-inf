for x in '0123456789ABCDEFGHIJKLMNOP':
    ok = True
    for y in '0123456789ABCDEFGHIJKLMNOP':
        a = '13'+ y + x + '5'
        b = '24' + y + '13'
        if (int(a,26)+ int(b,26)) % 8 != 0:
            ok = False
    if ok:
        a = '132' + x + '5'
        b = '24213'
        print((int(a,26)+int(b,26))//8)