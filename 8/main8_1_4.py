num = 0
count = 0
for n1 in "АВИОРТФ":
    for n2 in "АВИОРТФ":
        for n3 in "АВИОРТФ":
            for n4 in "АВИОРТФ":
                for n5 in "АВИОРТФ":
                    for n6 in "АВИОРТФ":
                        num += 1
                        col_n = 0
                        s = n1 + n2 + n3 + n4 + n5 + n6
                        for i in s:
                            if i == "Р":
                                col_n += 1
                        if (n1 != "О" and num % 2 == 0 and col_n == 2):
                            count += 1
                            print(num, n1, n2, n3, n4, n5, n6, col_n)
print(count)