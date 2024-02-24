def game(col_rocks, pl_position, v_hod1, v_hod2, v_hod3, winner): #р - позиция игрока. если четная, то значит, ход Вани, если нет - ход Пети 
    if pl_position == 3 and col_rocks >= winner:
        s = 1
    elif pl_position == 3 and col_rocks < winner:
        s = 0
    elif col_rocks >= winner and pl_position < 3:
        s = 0 
    else:
        if pl_position % 2 == 0:    # стратегия победителя 
            s1 = game(col_rocks + v_hod1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s2 = game(col_rocks + v_hod2, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s3 = game(col_rocks * v_hod3, pl_position + 1, v_hod1, v_hod2, v_hod3, winner) 
            s = s1 or s2 or s3
        else:                       # стратегия проигравшего
            s1 = game(col_rocks + v_hod1, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s2 = game(col_rocks + v_hod2, pl_position + 1, v_hod1, v_hod2, v_hod3, winner)
            s3 = game(col_rocks * v_hod3, pl_position + 1, v_hod1, v_hod2, v_hod3, winner) 
            s = s1 and s2 and s3
    return s

path = "/home/user/Documents/EGE inf/19/19/19_type1.json"

for s in range(1, 129):
    if game(s, 1,1,1, 2, 129) == 1:
        print(s)
        break