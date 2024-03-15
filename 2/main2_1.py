print("x w z y")
# x y w z переменные из задачи
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (not(not(x) or y) or (x == z) or w) == False:
# В данной формуле нужно менять условие в соответствии с условием задачи
                    print(x, w, z, y)

# отрицание - not
# конъюнкция(и, *) - and
# дизъюнкция(или, +) - or
# следование(импликация) - (not(x) or y) = (x -> y)
# тождество - ==