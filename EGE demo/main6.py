count = 0
for x in range(1, 10):
    for y in range(1, 10):
        if -x / 3 ** 0.5 + 10 > y > x / 3 ** 0.5:
            count += 1
print(count)