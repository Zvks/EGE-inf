num = 0
for n1 in "ABCD":
    for n2 in "ABCDE":
        for n3 in "ABCDE":
            for n4 in "ABCDE":
                for n5 in "BCDE":
                    num += 1
print(num)
print(4*5*5*5*4)