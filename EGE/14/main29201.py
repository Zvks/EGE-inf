x = 49**6 * 7 ** 19 - 7**9 - 21
count_6= 0
while x != 0:
    if x % 7 == 6:
        count_6 += 1
    x = x // 7
print(count_6)