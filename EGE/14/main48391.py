for x in "0123456789AB":
    for y in "0123456789AB":    
        if (int((y + 'AA' + x), 12) + int((x + '02' + y), 14)) % 80 == 0:
            print((int((y + 'AA' + x), 12) + int((x + '02' + y), 14)) / 80, x, y)
            break