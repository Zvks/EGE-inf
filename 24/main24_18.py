def pr(n): # функция, которая проверяет простое ли число
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

k=0
x = 550001

while k < 6:
    for i in range (2, int(x**0.5)+1):
        if x % i == 0:
            D = x//i
            if not(pr(D)):
                k += 1
                print (x, D)
                break
    x += 1