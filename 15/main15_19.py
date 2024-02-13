for A in range (0,100):
    OK = True
    for x in range (1,100):
        for y in range (1, 100):
            OK *= not( (x < A) and (y < A) and (x*y > 601))

    if OK: # истинность для любого х
        print (A)