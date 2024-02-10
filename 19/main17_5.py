f= open('17var01.txt')
p=[int(i) for i in f]
f.close()
k = 0
PP = 0
M = max(p)
for i in range(1,len(p)):
    if p[i-1] + p[i] == M:
        k+=1
        PP = max(PP, p[i-1]**2 + p[i]**2)

print(k,PP) 