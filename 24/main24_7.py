f=open('24var03.txt')
p= f.readline()
f.close()
N = float('inf') #верхняя граница минимума

for i in range(1,len(p)):
    if p[i-1]+p[i] == 'AB': #начинаем поиск подпоследовательности со строки АВ 
        k=1 #количество сочетаний АВ 
        n=2 #количество символов
        for j in range(i, len(p)-1):
            n+=1
            if p[j]+p[j+1] == 'AB':
                k += 1
            if k == 21:
                N = min (n, N)
                break         

print(N)