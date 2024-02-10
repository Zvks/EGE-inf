f=open("17var05.txt")
p= [int(i) for i in f]
f.close()
k=0
PP = -20000
for i in range(len(p)-1):
   if p[i]>0 and p[i]**0.5==int(p[i]**0.5) or p[i+1]>0 and p[i+1]**0.5==int(p[i+1]**0.5):
        k+=1
        PP = max(p[i]+p[i+1], PP)
print(k, PP)