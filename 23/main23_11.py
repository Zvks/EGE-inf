def f(x):
    if x == 71:
        return 1
    elif x > 71:
        return 0
    else:
        return f(x + 2) + f(x + 10)

print(f(5))