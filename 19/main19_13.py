"""     Игрок за один ход может добавить 1 или 4 камня либо 
    увеличить количество камней в кучев 3 раза """
"""     1 <= Начальное значение <= 201, игра заканчивается еслив куче >= 202 камня """

import json
def read_json(path):
    with open(path, "r") as fh:
        dict_ = json.load(fh)
    return dict_

def game(col_rocks, start_heap_1, pl_position, v_hod1, v_hod2, v_hod3, winner): #р - позиция игрока. если четная, то значит, ход Вани, если нет - ход Пети 
    if pl_position == 3 and col_rocks + start_heap_1 >= winner:
        s = 1
    elif pl_position == 3 and col_rocks + start_heap_1 < winner:
        s = 0
    elif col_rocks + start_heap_1 >= winner and pl_position < 3:
        s = 0 
    else:
        if pl_position % 2 == 0:    # стратегия победителя 
            s1 = game(col_rocks + v_hod1, start_heap_1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s2 = game(col_rocks + v_hod2, start_heap_1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s3 = game(col_rocks * v_hod3, start_heap_1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner) 
            s4 = game(col_rocks, start_heap_1 + v_hod1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s5 = game(col_rocks, start_heap_1 + v_hod2, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s6 = game(col_rocks, start_heap_1 * v_hod3, pl_position + 1, v_hod1, v_hod2, v_hod3, winner) 
            s = s1 or s2 or s3 or s4 or s5 or s6
        else:                       # стратегия проигравшего
            s1 = game(col_rocks + v_hod1, start_heap_1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s2 = game(col_rocks + v_hod2, start_heap_1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s3 = game(col_rocks * v_hod3, start_heap_1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner) 
            s4 = game(col_rocks, start_heap_1 + v_hod1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s5 = game(col_rocks, start_heap_1 + v_hod2, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s6 = game(col_rocks, start_heap_1 * v_hod3, pl_position + 1, v_hod1, v_hod2, v_hod3, winner) 
            s = s1 or s2 or s3 or s4 or s5 or s6
    return s

path = "/home/user/Documents/EGE inf/19/19/19_type1.json"
data = read_json(path)

for s in range(data['start_min'], data['winer']):
    if game(s, data['start_heap_1'], 1, data['v_hod1'], data['v_hod2'], data['v_hod3'], data['winer']) == 1:
        print(s)
        break