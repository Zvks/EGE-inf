f = open('17var01.txt')
p = [int(i) for i in f]
f.close()
m = float('inf')
count = 0
m3 = 0
for i in p:
    if i % 100 == 25:
        m = min (m, i)
for i in range(len(p) - 2):
    s = p[i] + p[i+1] + p[i + 2]
    if (10<= p[i] < 100) + (10 <= p[i+1] < 100) + (10 <= p[i+2] < 100) == 1 and s < m:
        count += 1
        m3 = max(m3, s )