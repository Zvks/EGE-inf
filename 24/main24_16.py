f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var13-17.txt')
file_list = f.readline()
f.close()
file_list = file_list.split('Z')
M = 0
for i in range(len(file_list)-1):
    M = max(M, len(file_list[i])+len(file_list[i+1]) + 1) # +1 так как Z не считается из-за split
print(M)  
