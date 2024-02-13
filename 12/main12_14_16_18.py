for i in range(0, 10000):
    s = ">" + "1"*11 + "2"*i + "3"*11 
    count = 0
    prost_mr = 0
    while (">1" in s) or (">2" in s) or (">3" in s):
        if (">1" in s):
            s = s.replace(">1", "222>", 1)
        elif (">2" in s):
            s = s.replace(">2", "3>", 1)
        elif (">3" in s):
            s = s.replace(">3", "1>", 1)
    for j in s:
        if j != '>':
            count += int(j)
    for n in range(2,count):
        if count % n == 0:
            prost_mr += 1
    if prost_mr == 0:
        print(i)
        break