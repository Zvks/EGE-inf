f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var07.txt')
file_list = f.readline()
f.close()
file_list = file_list.split('AB')
file_list = list(map(len, file_list))
M = 10**10
for i in range(len(file_list)-21):
    if M > sum(file_list[i:i+22]) + 44:
        print(file_list[i:i+22])
    M = min(M, sum(file_list[i:i+22]) + 2*22) # +22*2 так как AB не считается из-за split
print(M)  