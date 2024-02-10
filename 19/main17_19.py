f =open("17var15.txt")
p = [int(i) for i in f]
f.close()    
k = 0
PP = -float('inf')

for i in range(1,len(p)):
    if p[i-1] > 700 or  p[i] > 700:
        k += 1
        PP = max(p[i-1] **2 + p[i]**2, PP)                    

print(k, PP)