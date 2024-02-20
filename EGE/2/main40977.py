print("x w z y")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (not((not(y) or x) and (z or w)) or ((x and not(w)) or (y == z))) == False:
                    print(x, w, z, y)
