f = open("C:\\Users\\user\\ege_inf\\EGE-inf\\EGE\\17\\17_37337.txt")
pair = []
pairs = []
data = []
for s in f:
    n = int(s)
    data.append(n)
for i in range(len(data)- 1):
    for j in range(i+1, len(data)):
        pair = []
        if (data[i] % 160 != data[j] % 160) and (data[i] % 7 == 0 or data[j] % 7 == 0):
            pair.append(data[i])
            pair.append(data[j])
            pairs.append(pair)
print(len(pairs), max(pairs))