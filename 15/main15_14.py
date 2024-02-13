for A in range (1,1000):
    OK = True
    for x in range (1,500):
        OK *= ( (x % A != 0) <= ((x % 26 == 0) <= (x % 169 !=0)) ) # внимание, скобки!

    if OK: # истинность для любого х
        print (A)