k=0
x = 799999

while k < 5:
    M = 0
    for i in range (2, int(x**0.5)+1):
        if x % i == 0:
            M = x//i - i
            break
    if M % 17 == 0 and M != 0:
        k += 1
        print(x, M)
    x -= 1