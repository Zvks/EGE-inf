f = open('/home/user/Documents/EGE inf/EGE/26/26_2024.txt')
n = int(f.readline())
time_lst=[]
for s in f:
    start,end=map(int, s.split())
    time_lst.append([end, start])
time_lst.sort()

for i in range(time_lst):
    if 