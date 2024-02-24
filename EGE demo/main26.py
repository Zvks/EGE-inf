f = open('/home/user/Documents/EGE demo/®¯_ä ©«ë/ ¤ ­¨¥ 26/26_2024.txt')
n = int(f.readline())
a=[]
for s in f:
    start,end=map(int, s.split())
    a.append([end, start])
a.sort()
count=[]
z=0
for i in range(n):
    if z==0:
        z=a[i][0]
        count.append(a[i])
        last=i
    elif z<=a[i][1]:
        z=a[i][0]
        count.append(a[i])
        last=i
del count[-1]
z=count[-1][0]
for i in range (last, n):
    if z==0:
        z=a[i][0]
        count.append(a[i])
    elif z<=a[i][1]:
        count.append(a[i])
print(len(count), count[-1][1] - count[-2][0])