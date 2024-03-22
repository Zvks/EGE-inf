counter = 0
x = 860001
while counter < 5:
    M = 0
    for i in range (2, int(x**0.5)+1):
        if x % i == 0:  # i мин натуральный делитель x
            M = x // i - i # x // i макс натуральный делитель x
            break
    if M % 100 == 18:
        counter += 1
        print (x, M)
    x += 1