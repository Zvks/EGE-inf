f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var13-17.txt')
file_list = f.readline()
f.close()
file_list = file_list.replace('YX', 'Y X')
file_list = file_list.replace('ZX', 'Z X')
file_list = file_list.replace('ZY', 'Z Y')
file_list = file_list.split(' ')

print( max(map(len, file_list)))  
