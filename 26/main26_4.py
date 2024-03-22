f = open("C:\\Users\\user\\ege_inf\\EGE-inf\\26\\26\\26 вар4.txt")
data = []
for s in f:
    y_l, len_sq = map(int, s.split())
    data.append([y_l + len_sq, y_l])
data.sort()

podoshel = [data[0]]
max_dist = 0
for r_y, l_y in data[1:]:
    if l_y >= podoshel[-1][0]:
        podoshel.append([r_y,l_y])
    if len(podoshel) == 29 and l_y >= podoshel[-2][0]:
        max_dist = max(max_dist,l_y - podoshel[-2][1])

print(len(podoshel), max_dist)