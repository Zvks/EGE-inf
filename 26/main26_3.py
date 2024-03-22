file = open('C:\\Users\\user\\ege_inf\\EGE-inf\\26\\26\\26 вар4.txt')
n = file.readline()
data = []
print(file)
for st in file:
    start, time = st.split()
    data.append([int(start), int(start) + int(time)])
data.sort(key=lambda x: x[1])
res = [data[0]]
for i in range(1,len(data)):
    if res[-1][1] <= data[i][0]:
        print(data[i])
        res.append(data[i])
mx_break = 0
for i in range(len(data)):
    if res[-2][1] <= data[i][0]:
        mx_break = max(mx_break, data[i][0] - res[-2][1])
print(len(res), mx_break)