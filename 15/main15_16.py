for A in range (1,100):
    OK = True
    for x in range (1,100):
        OK *= ( (x % A != 0) <= ((x % 54 == 0) <= (162 % x !=0)) ) # внимание, скобки!

    if OK: # истинность для любого х
        print (A)