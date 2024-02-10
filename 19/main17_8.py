f= open('17var04.txt')
p=[int(i) for i in f]
f.close()
k = 0
P = float('inf')
M = max(p)
for i in range(2,len(p)):
    if  p[i-2]**2 + p[i-1]**2 + p[i]**2 > M and p[i-2]%10 != 3 and p[i-1]%10 != 3 and p[i]%10 != 3  :
        k+=1
        PP = min (PP, p[i-2]**2 + p[i-1]**2 + p[i]**2)

print(k,PP)

#можно использовать такое логическое условие (ни одно число не оканчивается на 3)
#bool(p[i-2]%10 == 3)+bool( p[i-1]%10 == 3)+bool( p[i]%10 == 3)==0