f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var18-20.txt')
file = f.readline()
f.close()
max_len = 0
counter = 1
for i in range(1,len(file)):
    if file[i-1] != file[i]:
        counter +=1
    else:
        max_len = max(counter,max_len)
        counter=1

print(max_len)