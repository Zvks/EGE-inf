vert = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],
        [4,6],[5,6],[6,6],[7,6],[8,6],[9,6],
        [7,10],[8,10],[9,10],[10,10],[11,10],
        [2,12],[3,12],[4,12],[5,12],[6,12],[7,12],[8,12],
        [15,8],[16,8],[17,8],[18,8],[19,8]]

gor = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],
       [10,2],[10,3],[10,4],[10,5],
       [12,7],[12,8],[12,9],
       [9,12],[9,13],[9,14],[9,15],[9,16],
       [15,4],[15,5],[15,6],[15,7]]
iskl = [[6,2],[6,3],[6,4],[6,5],
        [7,2],[7,3],[7,4],[7,5],
        [8,2],[8,3],[8,4],[8,5],
        [9,2],[9,3],[9,4],[9,5]]

def max_way():
    res = []
    for i in range(len(tabl), 0, -1):
        res_st = []
        for j in range(len(tabl[i])):
            print(i,j)
            if [i,j] == [0,0]:
                res_st.append(tabl[i][j])
            elif [i, j] in vert:                                # вертикальные исключения
                res_st.append(tabl[i][j]+max(res[i+1][j], 0))
            elif [i, j] in gor:                                 # горизонтальные исключения
                res_st.append(tabl[i][j]+max(0,res_st[j-1]))
            else:
                res_st.append(tabl[i][j]+max(res[i+1][j],res_st[j-1]))
        res.append(res_st)
    return res

def min_way():
    res = []
    for i in range(len(tabl), 0, -1):
        res_st = []
        for j in range(len(tabl[i])):
            print(i,j)
            if [i,j] == [0,0]:
                res_st.append(tabl[i][j])
            elif [i, j] in vert:                                # вертикальные исключения
                res_st.append(tabl[i][j]+min(res[i+1][j], 10**10))
            elif [i, j] in gor:                                 # горизонтальные исключения
                res_st.append(tabl[i][j]+min(10**10,res_st[j-1]))
            else:
                res_st.append(tabl[i][j]+min(res[i+1][j],res_st[j-1]))
        res.append(res_st)
    return res

file = open("C:\\Users\\user\\ege_inf\\EGE-inf\\18\\18var01.csv")
tabl = []

for s in file:
    st = list(map(int, s.split(",")))
    tabl.append(st)
    print(st)
file.close()
num_str = len(tabl) - 1
num_column = len(tabl[0]) - 1

print(max_way()[num_str][num_column], min_way()[num_str][num_column],min_way()[19][7], min_way()[11][9])