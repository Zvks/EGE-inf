f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var13-17.txt')
file_list = f.readline()
f.close()
file_list = file_list.replace('XY', 'X Y')
file_list = file_list.replace('XZ', 'X Z')
file_list = file_list.replace('YZ', 'Y Z')
file_list = file_list.split(' ')

print( max(map(len, file_list)))  
