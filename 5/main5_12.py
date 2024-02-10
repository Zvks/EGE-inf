for x in range(100,1000):
    a= x//100
    b = (x//10)%10
    c = x % 10
    p = a * b * c
    s = a + b + c

    if p == 240 and s == 19:
        c,b,a = sorted((a,b,c))
        print(a*100 + b*10 + c)
        break