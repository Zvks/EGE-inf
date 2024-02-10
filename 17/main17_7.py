f= open('17var03.txt')
p=[int(i) for i in f]
f.close()
k = 0
PP = 0
M = max(p)
for i in range(2,len(p)):
#в условии будем использовать исключающее ИЛИ (XOR) (ТОЛЬКО одно число оканчивается на 0) 
    if  (p[i-2] + p[i-1] + p[i] < M) and (bool(p[i-2]%10 == 0)^bool( p[i-1]%10 == 0)^bool(p[i]%10 == 0) == 1) :
        k+=1
        PP = max(PP, p[i-2] + p[i-1] + p[i])

print(k,PP) 