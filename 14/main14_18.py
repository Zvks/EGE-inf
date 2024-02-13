for x in '0123456789ABCDEFG':
    a = '135'+ str(x) + '9'
    b = '9' + str(x) + '531'
    c = int(a,17)+ int(b,17)
    if c % 9 == 0:
        print(c//9)