f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var13-17.txt')
file_list = f.readline()
f.close()
file_list = file_list.split('Z')
file_list = list(map(len, file_list))
M = 0
for i in range(len(file_list)-2):
    M = max(M, sum(file_list[i:i+3]) + 2) # +2 так как Z не считается из-за split
print(M)  
