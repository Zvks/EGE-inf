print("x w z y")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (not x or y ) or (z == x) or w:
                    print(x, w, z, y)