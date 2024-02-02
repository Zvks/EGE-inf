f = open('27/27/27v01_A.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(x) for x in f]
st = 10**10
fin = 10**10
summa = 10**10
for i in range(2*k,n):
    st = min(st, a[i-2*k])
    fin = min(fin, st + a[i-k])
    summa = min(summa, fin + a[i])
print(summa)