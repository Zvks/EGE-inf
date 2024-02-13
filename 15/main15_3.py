for A in range(1, 1_000):
    ok = True
    for x in range(1_000):
        for y in range(1_000):
            f = (x < 4) or (x >= 20) or (y >= 3*x + A) or (y < 100)
            if not f:
                ok = False
                break
    if ok:
        print(A)
        