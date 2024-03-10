x = 49**6 + 7**19 - 21
counter_0 = 0
while x > 0:
    if x % 7 == 0:
        counter_0 += 1
    x = x // 7
print(counter_0)