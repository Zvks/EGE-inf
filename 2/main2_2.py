print("x y w z")
for y in range(2):
    for x in range(2):
        for w in range(2):
            for z in range(2):
                if (not(not(y) or x) or (y == w) or z) == False:
                    print(x, y, w, z)