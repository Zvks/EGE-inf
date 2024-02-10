f =open("17var11.txt")
p = [int(i) for i in f]
f.close()    
k = 0
PP = 0
for i in range(len(p)-1):
    if abs(p[i])%10 == abs(p[i+1])%10 and abs(p[i])%2 == 1:
        k += 1
        PP = max(abs(p[i]) * abs(p[i+1]), PP)                    
 

print(k, PP)