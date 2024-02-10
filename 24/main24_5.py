f=open('24var01.txt')
p= f.readline()
f.close()
k=0
b=[]

for i in range(len(p)):
    if p[i] == 'A':
        k=1
        for j in range(i+1, len(p)):
            if p[j] == 'A':
                k += 1
            if k == 3:
                b.append(j-i+1)
                break         

print(max(b))