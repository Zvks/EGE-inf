def f(x, y):
    if x == y:
        return 1
    elif x > y or x == 18:
        return 0
    else:
        return f(x+1,y) + f(x+4,y) + f(x*2,y) 

print (f(4,11) * f(11,28))