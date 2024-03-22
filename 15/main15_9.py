B = [i for i in range(10,16)] 
C = [i for i in range(20,28)]
A = []

for x in range(100):
    if not( ((x in B) or (x in C)) <= (x in A) ):
        A.append(x)# добавляем в массив А все х, для которых выражение ложно
        print(x)
print(max(A) - min(A)) #находим разницу между макс и мин значением элементов массива
