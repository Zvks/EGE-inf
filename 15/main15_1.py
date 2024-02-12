for A in range(1, 1_000):
    ok = True
    for x in range(1_000):
        for y in range(1_000):
            f = (4*x + y < A) or (x < y) or (22 <= x)
            if not f:
                ok = False
                break
    if ok:
        print(A)
        break