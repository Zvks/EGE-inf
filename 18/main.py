# Элементы матрицы A обозначаются aij, где i - номер строки, в которой находится элемент, j - номер столбца.
# def dawn_(tabl_,str_, col_):
#     num_str = len(tabl)
#     num_column = len(tabl[0])
#     if str_< (num_str - 1)  and col_ < (num_column - 1):      
#         res = tabl_[str_][col_] + max(dawn_(tabl_, str_ + 1, col_ ), right_(tabl_, str_, col_ + 1))
#     elif str_== (num_str - 1)  and col_ == (num_column - 1):
#         res = tabl_[num_str - 1][num_column - 1]
#     return res

# def right_(tabl_,str_, col_):
#     num_str = len(tabl)
#     num_column = len(tabl[0])
#     if str_<= (num_str - 1)  and col_ <= (num_column - 1):     
#         res = tabl_[str_][col_] + max(dawn_(tabl_, str_ + 1, col_ ), right_(tabl_, str_, col_ + 1))
#     elif str_== (num_str - 1)  and col_ == (num_column - 1):
#         res = tabl_[num_str - 1][num_column - 1]
#     return res

def dawn_(tabl_,str_, col_):
    res = tabl_[str_ + 1][col_]
    return res

def right_(tabl_,str_, col_):
    res = tabl_[str_][col_+ 1]
    return res


file = open("/home/user/Documents/EGE inf/18/18_demo.csv")
tabl = []
money = []

for s in file:
    st = list(map(int, s.split(",")))
    tabl.append(st)
    print(st)
file.close()
num_str = len(tabl)
num_column = len(tabl[0])


print(dawn_(tabl, 0, 0), right_(tabl,0,0))
for i in range(len(tabl)- 1):
    for j in range(len(tabl)-1):
        money[i][j] = tabl[i][j]
        money[i][j+1] = right_(tabl, i, j)
        money[i+1][j]