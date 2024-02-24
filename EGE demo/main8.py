num = 0
for n1 in range(2,8):
    for n2 in range(8):
        for n3 in range(8):
            for n4 in range(8):
                for n5 in range(8):
                    if (n1 != n2 and n1 != n3 and n1 != n4 and n1 != n5) \
                        and (n2 != n3 and n2 != n4 and n2 != n5 and n2 != 1) \
                        and (n3 != n4 and n3 != n5 and n3 != 1)\
                        and (n4 != n5 and n4 != 1 )\
                        and (n5 != 1)\
                        and (n1 % 2 != n2 % 2 and n2 % 2 != n3 % 2 and n3 % 2 != n4 % 2 and n4 % 2 != n5 % 2):
                        num += 1
                        print(n1, n2, n3, n4, n5, num)
print(num)
# внимательно проверить все условия по выводу в терминале, алгоритм работает универсально 