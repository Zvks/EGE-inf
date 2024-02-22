# Элементы матрицы A обозначаются aij, где i - номер строки, в которой находится элемент, j - номер столбца.
n = 0
def max_down_right(i, j):
    i_max = len(tabl) - 1
    j_max = len(tabl[0]) - 1
    if i == i_max and j == j_max:       # правый нижний угол
        print("третья точка окончания",tabl[i][j])                                       
        return tabl[i][j]
    elif i < i_max and j < j_max:
        print("внутр")
        res = tabl[i][j] + max(max_down_right(i+ 1, j),max_down_right(i, j+1))
    elif i < i_max and j == j_max:                                              # правая граница квадрата
        res = tabl[i][j] + max_down_right(i+ 1, j)
    elif i == i_max and j < j_max:                                              # нижняя граница квадрата
        res = tabl[i][j] + max_down_right(i, j+1)

    elif i in [4,5,6,7,8,9] and j == 1:                                         # правая внутренняя граница 1 угла
        print("правая внутренняя граница 1 угла")
        res = tabl[i][j] + max_down_right(i+ 1, j)
    elif i == 3 and j in [2,3,4,5]:                                             # нижняя внутренняя граница 1 угла
        print("нижняя внутренняя граница 1 угла")                                      
        res = tabl[i][j] + max_down_right(i, j+ 1)

    elif i in [15,16,17,18,19] and j == 7:                                   # правая внутренняя граница 2 угла
        print("првая внутренняя граница 2 угла")
        res = tabl[i][j] + max_down_right(i+ 1, j)
    elif i == 14 and j in [4,5,6,7]:                                          # нижняя внутренняя граница 2 угла
        print("нижняя внутренняя граница 2 угла")
        res = tabl[i][j] + max_down_right(i, j+ 1)

    elif i in [7,8,9,10,11] and j == 9:                                   # правая внутренняя граница 3 угла
        print("првая внутренняя граница 3 угла")
        res = tabl[i][j] + max_down_right(i+ 1, j)
    elif i == 11 and j in [7,8,9]:                                          # нижняя внутренняя граница 3 угла
        print("нижняя внутренняя граница 3 угла")
        res = tabl[i][j] + max_down_right(i, j+ 1)

    elif i in [2,3,4,5,6,7,8] and j == 11:                                   # правая внутренняя граница 4 угла
        print("нижняя внутренняя граница 4 угла")
        res = tabl[i][j] + max_down_right(i+ 1, j)
    elif i == 8 and j in [12,13,14,15,16]:                                          # нижняя внутренняя граница 4 угла
        print("нижняя внутренняя граница 4 угла")
        res = tabl[i][j] + max_down_right(i, j+ 1)

    elif i == 19 and j == 7:                                                # первая точка окончания
        print("первая точка окончания")
        res = tabl[i][j]
    elif i == 11 and j == 9:                                                 # вторая точка окончания
        print("вторая точка окончания")                                              
        res = tabl[i][j]
    global n
    n += 1
    print(n)
    return res

""" def min_down_right(i, j):
    if i == 0 and j == 0:
        res = tabl[i][j]
    elif i > 0 and j > 0:
        res = tabl[i][j] + min(min_down_right(i- 1, j),min_down_right(i, j-1))
    elif i > 0 and j == 0:                                                      # верхняя граница квадрата
        res = tabl[i][j] + min_down_right(i- 1, j)
    elif i == 0 and j > 0:                                                      # левая граница квадрата
        res = tabl[i][j] + min_down_right(i, j-1)
    return res
     """
file = open("/home/user/Documents/EGE inf/18/18var01.csv")
tabl = []
money = []

for s in file:
    st = list(map(int, s.split(",")))
    tabl.append(st)
    print(st)
file.close()
num_str = len(tabl)
num_column = len(tabl[0])


#print(max_down_right(0, 0), min_down_right(9,9))
print(max_down_right(0, 0))
