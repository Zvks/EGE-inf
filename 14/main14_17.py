for x in '0123456789ABCDE':
    a = '135'+ str (x) + '7'
    b = '7' + str (x) + '531'
    c = int (a,15)+ int (b,15)
    if c % 14 == 0:
        print (c//14)
        break