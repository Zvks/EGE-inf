#         [8,12],[8,13],[8,14],[8,15],[8,16],
#         [14,4],[14,5],[14,6],[14,7]]
vert = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],
[4,4],[5,4],[6,4],[7,4],[8,4],[9,4],[10,4],[11,4],[12,4],[13,4],
[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7],
[13,12],[14,12],[15,12],[16,12],[17,12],[18,12],[19,12],
[5,18],[6,18],[7,18],[8,18],[9,18],[10,18],[11,18],[12,18],[13,18],[14,18]
]

gor = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],	[0,14],	[0,15],	[0,16],	[0,17],	[0,18],	[0,19],
[4,1],	[4,2],	[4,3],	[4,4],
[9,7],	[9,8],	[9,9],	[9,10],	[9,11],	[9,12],
[13,8],	[13,9],	[13,10],	[13,11],
[15,15],	[15,16],	[15,17]]
iskl = []






def max_way():
    res = []
    for i in range(len(tabl)):
        res_st = []
        for j in range(len(tabl[i])):
            print(i,j)
            if [i,j] == [0,0]:
                res_st.append(tabl[i][j])
            elif [i, j] in vert:                                # вертикальные исключения
                res_st.append(tabl[i][j]+max(res[i-1][j], 0))
            elif [i, j] in gor:                                 # горизонтальные исключения
                res_st.append(tabl[i][j]+max(0,res_st[j-1]))
            else:
                res_st.append(tabl[i][j]+max(res[i-1][j],res_st[j-1]))
        res.append(res_st)
    return res

def min_way():
    res = []
    for i in range(len(tabl)):
        res_st = []
        for j in range(len(tabl[i])):
            print(i,j)
            if [i,j] == [0,0]:
                res_st.append(tabl[i][j])
            elif [i, j] in vert:                                # вертикальные исключения
                res_st.append(tabl[i][j]+min(res[i-1][j], 10**10))
            elif [i, j] in gor:                                 # горизонтальные исключения
                res_st.append(tabl[i][j]+min(10**10,res_st[j-1]))
            else:
                res_st.append(tabl[i][j]+min(res[i-1][j],res_st[j-1]))
        res.append(res_st)
    return res

file = open("/home/user/Documents/EGE demo/®¯_ä ©«ë/ ¤ ­¨¥ 18/18_2024.csv")
tabl = []

for s in file:
    st = list(map(int, s.split(",")))
    tabl.append(st)
    print(st)
file.close()
num_str = len(tabl) - 1
num_column = len(tabl[0]) - 1

print(max_way()[num_str][num_column], min_way()[num_str][num_column],min_way()[19][11], min_way()[14][17])