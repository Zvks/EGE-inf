
f=open('27v05_A.txt','r')
st = f.readlines() # создаем массив из строк файла
f.close()
N = int(st[0]) # записываем количество строк в переменную N
del (st[0]) # удаляем первую строку
s = 0 # создаем переменную для суммы
min_r = 10000
for i in range(N):
    a, b = map(int, st[i].split()) #разделяем строку на две переменные
    s += max(a,b) # накапливаем сумму из максимальных значений 
    m = abs (a-b)  #находим разницу между значениями одной строки
    if m % k !=0:
        min_r=min (m, min_r) #мин. разница, которая не делится на k

if s % k!=0:
    print (s)
else:
    print (s - min_r)