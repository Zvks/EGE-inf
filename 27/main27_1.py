f = open('27/27/27v0')           # открывает файл
k = int(f.readline())                   # считывает первые две строки в переменные k и n
n = int(f.readline())
a = [int(x) for x in f]                 # считывает оставшиеся строки из файла и преобразует их в список чисел, сохраняя его в переменной a
min1 = 10**10
min2 = 10**10
summa = 10**10
for i in range(2*k,n):                  # код выполняет цикл для каждого числа i в диапазоне от 2k до n
    min1 = min(min1, a[i-2*k])              # код находит минимальное значение st из предыдущих 2k чисел списка a
    min2 = min(min2, min1 + a[i-k])         # код находит минимальное значение fin, добавляя к значению st следующее число списка a, с индексом i-k
    print(i, a[i-k], i-k)
    summa = min(summa, min2 + a[i])      # код находит минимальное значение summa, добавляя к значению fin следующее число списка a, с индексом i.
    print(k*2, n, i, min1, min2, summa)
print(summa)
