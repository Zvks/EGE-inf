f = open("/home/user/Documents/EGE demo/®¯_ä ©«ë/ ¤ ­¨¥ 9/9_2024.csv")
col_str = 0
for s in f:
    string = list(map(int, s.split(";")))
    col_dupl = 0
    dupl = []
    for i in string:
        if string.count(i) == 2:
            col_dupl += 1
            dupl.append(i)
    if (col_dupl == 4) and (sum(string)/ len(string) > sum(dupl)/ len(dupl)):
        col_str += 1
        print(string)
print(col_str)
    