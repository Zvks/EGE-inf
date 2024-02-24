for A in range (0,1000):
    OK = True
    for x in range (0,1000):
        for y in range (0, 1000):
            OK *= ((x + 2*y) < A or (y > x) or(x > 60))

    if OK: # истинность для любого х
        print (A)
        break