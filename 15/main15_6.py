def d(n, m):
    if n % m == 0: #проверка на делимость
        return 1

for A in range (1,1000):
    OK = True
    for x in range (1,1000):
        OK*=( not(d(x,20)) or not(d(x,11)) or (x + A) >= 300 )
    if OK: # истинность для любого х
        print (A)
        break