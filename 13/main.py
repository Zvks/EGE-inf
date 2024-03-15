print(bin(255)[2:], bin(255)[2:], bin(255)[2:], bin(224)[2:])
print(bin(116)[2:], bin(29)[2:], bin(170)[2:], bin(89)[2:])
cnt = 0
for n1 in range(2):
    for n2 in range(2):
        for n3 in range(2):
            for n4 in range(2):
                for n5 in range(2):
                    if (n1+n2+n3+n4+n5) <= 3:
                        cnt += 1
print(cnt)