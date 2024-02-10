f=open('24var04.txt')
p= f.readline()
f.close()
N = 0 #нижняя граница максимума

for i in range(len(p)):
    n = 1 #количество символов всего
    k = 0 #количество сочетаний АВ
    for j in range (i+1, len(p)):
        n += 1
        if p[j-1]+p[j] == 'AB': #поиск сочетаний АВ 
            k += 1
        if k == 22:
            N = max(n-1, N) # убираем одну букву из сочетания АВ и ищем максимум
            break          

print(N)