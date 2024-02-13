def treug(n, m, k):    
    if n <  m + k and m < k + n and k < n + m: 
        return 1
    else: return 0


for A in range (1,100):
    OK = True

    for x in range (1,100):
        OK*= (not((treug(x, 12, 20) == (not(max(x, 5) > 28))) and treug(x, A, 3)))
    if OK: # истинность для любого х
        print (A)