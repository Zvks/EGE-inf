for x in range(100,1000):
    a= x//100
    b = (x//10)%10
    c = x % 10
    if (a ** 2 + b**2 == 97 and b**2 + c**2 == 52) or (a ** 2 + b**2 == 52 and b**2 + c**2 == 97):
        c, a = sorted((a, c))     

        print(a*100 +b*10+c)
        break