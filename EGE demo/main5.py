list = []
for N in range(100):
    n = bin(N)[2:]
    if N % 3 == 0:
        n += n[-3:]
    else:
        n += bin((N % 3)*3)[2:]
    if int(n, 2)> 151:
        print(N, int(n, 2))
        list.append(int(n, 2))
print(min(list))
#        break
# Первое число удвл данному условию не является минимальным т. к. зависимость не линейная