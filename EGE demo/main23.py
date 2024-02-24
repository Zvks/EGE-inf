def Func(x, y):
    if x == y:
        return 1
    elif x > y or x == 11:
        return 0
    else:
        return Func(x+1, y) + Func(x*2, y) + Func(x**2, y)

print(Func(2,20))