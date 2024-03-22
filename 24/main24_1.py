f=open('C:\\Users\\user\\ege_inf\\EGE-inf\\24\\24\\24var01.txt')
file_list = f.readline()
f.close()
index_list = [] # массив для индексов букв А
min_posl = 10**10
for i in range(len(file_list)):# в файле ищем буквы А и их индексы добавляем в cписок
    if file_list[i] == 'A':
        index_list.append(i)

for i in range (len(index_list)- 2023): # в ищем подпоследовательности длиной 2024 символа
    #print(index_list[i])
    min_posl = min(min_posl, (index_list[i + 2023] - index_list[i]) + 1) # 2024 = 2023 - 0 + 1 нумерация с нуля
print(min_posl)