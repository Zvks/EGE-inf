f = open("/home/user/Documents/EGE inf/EGE/27/27-A.txt")
n = int(f.readline())
num_list = f.readlines()
pair = 0
zag = []

for j in range(0,len(num_list)-14):
    for i in range(j + 14, len(num_list)):
        if ((int(num_list[j]) + int(num_list[i])) % 8 == 0) and ((int(num_list[j]) * int(num_list[i])) % 19683 == 0):
            pair += 1
print(pair, len(num_list))
# A
