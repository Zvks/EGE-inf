def d(n, m):
    if n % m == 0: #проверка на делимость
        return 1

for A in range (1,1000):
    OK = True
    for x in range (1,1000):
        OK = OK*( not(d(x,13)) or not(d(x,21)) or (x + A) >= 500 )
    if OK: # истинность для любого х
        print (A)
        break