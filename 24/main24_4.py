f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var04.txt')
file_list = f.readline()
f.close()
file_list = file_list.replace("E", "")
#print(file_list)
index_list = [] # массив для индексов букв А
max_posl = 0
for i in range(len(file_list)):# в файле ищем буквы А и их индексы добавляем в cписок
    if file_list[i] == 'A':
        index_list.append(i)

for i in range (len(index_list)- 700): # в ищем подпоследовательности длиной 700 символа
    max_posl = max(max_posl, (index_list[i + 700] - index_list[i]) + 1) # 700 = 699 - 0 + 1 нумерация с нуля
print(max_posl)

# f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var04.txt')
# file_list = f.readline()
# f.close()
# file_list = file_list.split("E")
# max_posl = 0
# for i in file_list:
#     if i.count("A") <= 700:
#         max_posl = max(max_posl, len(i))
# print(max_posl)