for i in range(4, 10000):
    s = "1" + "2"*i  
    count = 0
    while ("12" in s) or ("3322" in s) or ("2222" in s):
        if ("12" in s):
            s = s.replace("12", "33", 1)
        elif ("2222" in s):
            s = s.replace("2222", "1", 1)
        elif ("3322" in s):
            s = s.replace("3322", "21", 1)
    for j in s:
        count += int(j)
    if count == 218:
        print(i)
        break
