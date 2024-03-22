counter = 0
x = 850001
while counter < 6:
    F = 0
    for i in range (2, int(x**0.5)+1):
        if x % i == 0:
            F = x // i - i
            break
    if F % 7 == 0 and F != 0:
        counter += 1
        print(x, F)
    x += 1