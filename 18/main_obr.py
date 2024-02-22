# # первая цифра меняется - i, вторая нет
# vert = [[0,19],[1,19],[2,19],[3,19],[4,19],[5,19],[6,19],[7,19],[8,19],[9,19],[10,19],[11,19],[12,19],[13,19],[14,19],[15,19],[16,19],[17,19],[18,19],[19,19], # вертикальная конечная
#         [4,1],[5,1],[6,1],[7,1],[8,1],[9,1],
#         [7,9],[8,9],[9,9],[10,9],[11,9],                
#         [15,7],[16,7],[17,7],[18,7],[19,7],
#         [2,11],[3,11],[4,11],[5,11],[6,11],[7,11],[8,11]]         
# # вторая цифра меняется - j, первая нет  
# gor = [[19,0],[19,1],[19,2],[19,3],[19,4],[19,5],[19,6],[19,7],[19,8],[19,9],[19,10],[19,11],[19,12],[19,13],[19,14],[19,15],[19,16],[19,17],[19,18],[19,19], # вертикальная конечная
#         [3,2],[3,3],[3,4],[3,5],
#         [11,7],[11,8],[11,9],
#         [8,12],[8,13],[8,14],[8,15],[8,16],
#         [14,4],[14,5],[14,6],[14,7]]

vert = [[0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9]]

gor = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9]]

def up(i,j):
    return i-1, j  

def down(i,j):
    return i+1, j  

def right(i,j):
    return i, j+1  

def left(i,j):
    return i, j+1  

def diog_up_right(i,j):
    return i-1, j+1  

def diog_down_left(i,j):
    return i+1, j-1  

def diog_up_left(i,j):
    return i-1, j-1  

def diog_down_right(i,j):
    return i+1, j+1 


def max_way(i, j):
    if ([i,j] in vert) and ([i,j] in gor):       # угол     
        #print("угол",i, j)                                 
        res = tabl[i][j]
    elif [i,j] in vert:                                              # верт граница
        #print("верт граница", i, j)
        res = tabl[i][j] + max_way(up(i,j))
    elif [i,j] in gor:                                              # гор граница
        #print("гор граница", i, j)
        res = tabl[i][j] + max_way(right(i,j))
    elif not(i in vert) and not(j in gor):
        #print("внутр", i, j)
        res = tabl[i][j] + max(max_way(up(i,j)),max_way(right(i,j)))
    return res

file = open("/home/user/Documents/EGE inf/18/18_demo.csv")
tabl = []

for s in file:
    st = list(map(int, s.split(",")))
    tabl.append(st)
    print(st)
file.close()
num_str = len(tabl)
num_column = len(tabl[0])

#print(max_way(9,0))