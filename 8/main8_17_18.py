num = 0
for n1 in range(1,8):
    for n2 in range(8):
        for n3 in range(8):
            for n4 in range(8):
                if (n1 == n2 and n1 != n3 and n1 != n4 and n3 != n4) \
                    or (n2 == n3 and n2 != n4 and n3 != n1 and n1 != n4) \
                    or (n3 == n4 and n3 != n2 and n1 != n3 and n1 != n2):
                    num += 1
                    print(n1, n2, n3, n4, num)
print(num)