import math 
alf = int(input())
col_symb =int(input())
col_x = int(input())
k = 1
while alf >= 2:
    alf //= 2
    k +=1
print(k)
a = math.ceil((col_symb * k) / 8) * col_x / 1024
print(a)