f=open('26/26/26var07.txt')
st = f.readlines() # создаем массив из строк файла
f.close()
N1,N2 = map (int, st[0].split())  # записываем количество строк в переменную N1, N2
del (st[0]) # удаляем первую строку
A=[]
B=[]
C=[]
D=[]

for i in range(N2):
    a, b =map (int, st[i].split()) #разделяем строку на две переменные
    A.append(a)
    B.append(b)

for i in range(N2,N1):
     A.append( int(st[i]) )
A.sort (reverse=True)

for i in A:
    for j in B:
        if i == j:   C.append(i) #Запишем в массив все стороны коробок, для которых есть замочки       

x = C[0]
D.append(x)

for i in C:
    if x - i >=6:
        x = i
        D.append(x) #В массив D запишем стороны, удовлетворяющие условию о разнице между длинами сторон  

print(len(D), min(D))