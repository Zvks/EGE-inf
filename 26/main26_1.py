file = open('C:\\Users\\user\\ege_inf\\EGE-inf\\26\\26\\26 вар1.txt')
n = file.readline()
data = []
print(file)
for st in file:
    start, time = st.split()
    data.append([int(start), int(start) + int(time)]) # в список data добавляются время начала и время конца(длительность + время начала)
data.sort(key=lambda x: x[1]) # data сортируется по возрастанию последнего элемента
res = [data[0]]
for i in range(1,len(data)):
    if res[-1][1] <= data[i][0]: # если время окончания мероприятия меньше или равно времени начала следующего 
        res.append(data[i]) # то 
mx_break = res[-1][1] - res[-2][0]
for i in range(len(data)):
    if res[-2][1] <= data[i][0]:
        print(res[-2][1])
        mx_break = max(mx_break, data[i][0] - res[-2][1])
print(len(res), res, mx_break)