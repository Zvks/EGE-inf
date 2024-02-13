for A in range (1,500):
    OK = True
    for x in range (1,500):
        OK *= ( (x % A != 0) <= ((x % 18 == 0) <= (x % 81 !=0)) ) # внимание, скобки!

    if OK: # истинность для любого х
        print (A)