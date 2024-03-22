f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var08.txt')
file_list = f.readline()
f.close()

file_list = file_list.split('AB')
file_list = list(map(len, file_list))
M = 0
for i in range(len(file_list)-21):
    M = max(M, sum(file_list[i:i+22]) + 2*22) # +22*2 так как AB не считается из-за split
print(M)  



