k=0
x = 860001
while k < 5:
    M = 0
    for i in range (2, int(x**0.5)+1):
        if x % i == 0:
            M = x // i - i
            break
    if M % 100 == 18:
        k += 1
        print (x, M)
    x += 1