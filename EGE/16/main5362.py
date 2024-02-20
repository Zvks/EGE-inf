def Func(n):
    if n <= 2:
        res = n + 1
    elif n > 2:
        res = 2*Func(n - 1) + Func(n - 2)
    return res
print(Func(4))