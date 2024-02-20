def game(col_rocks, start_heap_1, pl_position, v_hod1, v_hod2, v_hod3, winner):
    #print(col_rocks, pl_position) #р - позиция игрока. если четная, то значит, ход Вани, если нет - ход Пети 
    if ( pl_position == 3) and col_rocks + start_heap_1 >= winner:
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
            s = s1 and s2 and s3 and s4 and s5 and s6
    return s

for s in range(69, 1, -1):

    if game(s, 8, 1, 1, 1, 2, 77) == 1:
        print(s)
