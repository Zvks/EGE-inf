def Func(x, y):
    if x == y:
        return 1
    elif y < x:
        return 0
    else:
        return Func(x*2, y) + Func(x + 1, y)
print(Func(1, 10)* Func(10, 21)* Func(21, 30))
print(bin(240), bin(137), int("10000000", 2))