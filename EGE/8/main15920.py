counter = 0
for n1 in "АГИЛМОРТ":
    for n2 in "АГИЛМОРТ":
        for n3 in "АГИЛМОРТ":
            for n4 in "АГИЛМОРТ":
                counter += 1
                if (n1 == "Г" and n2 == "О"):
                    print(counter)
                    break
print(int("1500", 8)+1)