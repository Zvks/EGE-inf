for A in range(1, 500):
    ok = True
    for x in range(500):
        f = ((120 % A == 0) and (not(x % A != 0) or (not(x % 18 == 0) or not(x % 24 == 0))))
        if not f:
            ok = False
            break
    if ok:
        print(A)
        