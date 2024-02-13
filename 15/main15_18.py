for A in range (0,100):
    OK = True
    for x in range (1,100):
        for y in range (1, 100):
            OK *= ( (x >= A) or (y >= A) or (x*y <= 270))

    if OK: # истинность для любого х
        print (A)