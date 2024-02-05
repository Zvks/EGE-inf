f=open('26/26/26var08.txt')
st = f.readlines() # создаем массив из строк файла
f.close()

N1,N2 = map (int, st[0].split())  # записываем количество строк в переменную N1, N2
del (st[0]) # удаляем первую строку

A=[]
B=[]
C=[]

for i in range(N2):
    a, b =map (int, st[i].split()) #разделяем строку на две переменные
    A.append(a)
    B.append(b)

for i in range(N2,N1):
     A.append( int(st[i]) )
A.sort (reverse=True)
B.sort (reverse=True)

def ma(b):
    for a in A:
        if b - a >= 5:
            C.append(a)
            return mb(a)

def mb (a):
    for b in B:
        if a - b >= 5:
            C.append(b)
            return ma(b)      

x = max(A[0], B[0])
C.append(x)
if x in B:
    ma(x)
else:
    mb(x)       

print(len(C), min(C))