f=open("17var09.txt")
p= [int(i) for i in f]
f.close()       
k = 0
PP = -20000
for i in range(len(p)-1):
    if p[i]%10 == 5 and p[i+1]%10 == 5:
        k += 1
        PP = max(abs(p[i]-p[i+1]), PP)
print(k, PP)