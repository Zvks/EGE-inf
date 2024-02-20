count = 0
for w in "АМУХ":
    for x in "АМУХ":
        for y in "АМУХ":
            for z in "АМУХ":
                count += 1
                if (w + x + y + z) == "ХУХХ":
                    print(w, x, y, z, count)
                    break