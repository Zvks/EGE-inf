f =open("17var12.txt")
p = [int(i) for i in f]
f.close()  
k = 0
PP = float('inf')
for i in range(1,len(p)):
    if abs(p[i-1])%10 != abs(p[i])%10 and abs(p[i-1])%2 == 1 and abs(p[i])%2 == 1:
        k += 1
        PP = min(abs(p[i]) * abs(p[i+1]), PP)                    

print(k, PP)