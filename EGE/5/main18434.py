for i in range(100):
    n = bin(i)[2:]
    n = n + bin(n.count("1")%2)[2:]
    n = n + bin(n.count("1")%2)[2:]
    print(i, n, int(n, 2))
    if int(n, 2) > 55:
        print(i, n, int(n, 2))