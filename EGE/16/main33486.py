# F(0) = 0;
# F(n) = n + F(n − 3), если n mod 3  =  0, и n > 0;
# F(n) = n + F(n − (n mod 3)), если n mod 3 > 0.
# Чему равно значение функции F(26)?
def Func(n):
    if n == 0:
        res = 0
    elif (n % 3 == 0) and (n > 0):
        res = n + Func(n - 3)
    elif (n % 3 > 0):
        res = n + Func(n - (n % 3))
    return res

print(Func(26))
 