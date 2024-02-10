f=open('24var05-08.txt')
s= f.readline()
f.close()
m=0
s = s.split('000')
for i in s:
    m = max(m, len(i))   
print (m+4)#добавляем к слову первые 00 и последние 00

#или

s = s.replace('000', '00 00')
s = s.split(' ')
print (max (map (len, s)))