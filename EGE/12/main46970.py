break_key = False
for n1 in range(50):
    if break_key == False:
        for n2 in range(50):
            if break_key == False:
                for n3 in range(50):
                    s = "0" + n1 * "1" +n2 * "2" + n3 * "3" + "0"
                    while not("00" in s):
                        s = s.replace("01", "210", 1)
                        s = s.replace("02", "3101", 1)
                        s = s.replace("03", "2012", 1)
                    if s.count("1") == 70 and s.count("2") == 56 and s.count("3") == 23:
                        break_key = True
                        print(n1+ n2+ n3 + 2)
                        break