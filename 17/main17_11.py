f=open("17var07.txt")
p= [int(i) for i in f]
f.close()
k = 0
PP = -20000
for i in range(len(p)-1):
    if p[i]%3 == 0 and p[i+1]%3 == 0:
        k += 1
        PP = max(p[i] + p[i+1], PP)
print(k, PP)