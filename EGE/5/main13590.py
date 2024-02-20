for i in range(100, 1000):
    n1 = i % 10
    n2 = i // 10 % 10
    n3 = i // 100
    num_1 = n1 * n2
    num_2 = n2 * n3
    res = str(max(num_1, num_2)) + str(min(num_1, num_2))
    if res == "205":
        print(i)