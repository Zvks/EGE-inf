f =open("17var13.txt")
p = [int(i) for i in f]
f.close()    
k = 0
PP = -float('inf') #бесконечно малое число
for i in range(1,len(p)):
    if p[i-1] + p[i] >=100 and (p[i-1] < 0 or p[i]<0):
        k += 1
        PP = max(p[i-1] * p[i], PP)                    

print(k, PP)