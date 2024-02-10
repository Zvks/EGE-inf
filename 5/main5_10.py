for x in range(100,1000):
    a= x//100
    b = (x//10)%10
    c = x % 10

    if (a ** 2 + b**2 == 74 and b**2 + c**2 == 34) or (a ** 2 + b**2 == 34 and b**2 + c**2 == 74):
        c, a = sorted((a, c))      

        print(a*100 +b*10+c)
        break