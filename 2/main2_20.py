print("x y w z")
for y in range(2):
    for x in range(2):
        for w in range(2):
            for z in range(2):
                if (not((x == y) or (x == w)) or z or not(not(y) or w)) == False:
                    print(x, y, w, z)