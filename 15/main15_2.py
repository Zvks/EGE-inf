for A in range(1, 500):
    ok = True
    for x in range(500):
        for y in range(500):
            f = (x**2 + y**2 > 128) or (y < 0 - x + A)
            if not f:
                ok = False
                break
    if ok:
        print(A)
        break