for A in range(1, 500):
    ok = True
    for x in range(500):
        for y in range(500):
            f = (x >= 20) or (y >= 40) or (y <= x + A) or (y >= 3*x - A)
            if not f:
                ok = False
                break
    if ok:
        print(A)
        break