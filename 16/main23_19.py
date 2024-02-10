def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        return f(x+3,y) + f(x+4,y) + f(x*3,y) 

print (f(1,7) * f(7,30)) 