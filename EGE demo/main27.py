f = open("/home/user/Documents/EGE demo/®¯_ä ©«ë/ ¤ ­¨¥ 27/27_B_2024.txt")



k = int(f.readline())
n = int(f.readline())
a = [int(x) for x in f]
st = 0
fin = 0
summa = 0
for i in range(2 * k, n):
    st = max(st, a[i-2*k])
    fin = max(fin, st + a[i-k])
    summa = max(summa, fin + a[i])
print(summa)