for A in range(500):
    ok = True
    for x in range(500):
        f = (x&51 == 0 or (not(x&41 == 0) or x&A == 0))
        if not f:
            ok = False
            break
    if ok:
        print(A)
        #break