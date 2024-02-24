def Func(n):
    if n > 2024:
        res = n
    else:
        res = n * Func(n+1)
    return res
print(Func(2022)/ Func(2024))