res = []
for i in range(174457,174505):
    count = 0
    for j in range(2, i//2 + 1):
        if i%j == 0:
            count += 1
            if count > 2:
                break
        if count == 2 and j == i//2:
            res.append(i)
print(res)
for i in res:
    for j in range(2, i//2 + 1):
        if i%j == 0:
            print(j, i /j)
            break
