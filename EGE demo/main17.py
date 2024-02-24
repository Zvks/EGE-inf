f = open("/home/user/Documents/EGE demo/®¯_ä ©«ë/ ¤ ­¨¥ 17/17_2024.txt")
end_13 = []
threes = []
data = []

for i in f:
    data.append(int(i))
for i in data:
    if int(i) % 100 == 13:
        end_13.append(int(i))
three_znach = 0
max_end_13 = max(end_13)
for i in range(1,len(data)-1):
    three_znach = 0
    if (data[i-1]//100 <= 9) and (data[i-1]//100 > 0):
        three_znach += 1
    if (data[i]//100 <= 9) and (data[i]//100 > 0):
        three_znach += 1
    if  (data[i+1]//100 <= 9) and (data[i+1]//100 > 0):
        three_znach += 1
    
    if ((three_znach == 2) and ((data[i-1] + data[i] + data[i+1]) <= max_end_13)) :
        three_sum = data[i-1] + data[i] + data[i+1]
        print(data[i-1], data[i], data[i+1])
        threes.append(three_sum)
print(len(threes),max(threes))