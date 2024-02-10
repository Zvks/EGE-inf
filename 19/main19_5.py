"""     Игрок за один ход может добавить 1 или 4 камня либо 
    увеличить количество камней в кучев 3 раза """
"""     1 <= Начальное значение <= 201, игра заканчивается еслив куче >= 202 камня """

import json
def read_json(path):
    with open(path, "r") as fh:
        dict_ = json.load(fh)
    return dict_

def game(col_rocks, pl_position, v_hod1, v_hod2, winner): #р - позиция игрока. если четная, то значит, ход Вани, если нет - ход Пети 
    if pl_position == 3 and col_rocks >= winner:
        s = 1
    elif pl_position == 3 and col_rocks < winner:
        s = 0
    elif col_rocks >= winner and pl_position < 3:
        s = 0 
    else:
        if pl_position % 2 == 0:    # стратегия победителя 
            s1 = game(col_rocks + v_hod1, pl_position + 1, v_hod1, v_hod2, winner)
            s2 = game(col_rocks * v_hod2, pl_position + 1, v_hod1, v_hod2, winner) 
            s = s1 or s2
        else:                       # стратегия проигравшего
            s1 = game(col_rocks + v_hod1, pl_position + 1, v_hod1, v_hod2, winner)
            s2 = game(col_rocks * v_hod2, pl_position + 1, v_hod1, v_hod2, winner)
            s = s1 and s2
    return s
path = "/home/user/Documents/EGE inf/19/19/19_type2.json"
data = read_json(path)

for s in range(data['start_min'], data['winer']):
    if game(s, 1, data['v_hod1'], data['v_hod2'], data['winer']) == 1:
        print(s)
        break
