def f(n):
    if n == 49:
        return 1
    elif n > 49:
        return 0
    else:
        return f(n+2) + f(n+7)

print(f(5))