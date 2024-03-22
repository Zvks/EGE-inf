def pr(D): # функция, которая проверяет простое ли число
    res = False
    for i in range(2, int(D**0.5)+1):
        if D % i == 0:
            res = True
    return res

counter = 0
x = 550001

while counter < 6:
    for i in range (2, int(x**0.5)+1): # делители числа симметричны
        if x % i == 0:                 
            D = x//i                   # макс дел числа это разность числа и мин дел
            if (pr(D)):
                counter += 1
                print (x, D)
                break
    x += 1