def game(col_rocks, start_heap_1, pl_position, v_hod1, v_hod2, v_hod3, winner):
    if (pl_position == 5 or pl_position == 3) and col_rocks + start_heap_1 >= winner:
        s = 1
    elif pl_position == 5 and col_rocks + start_heap_1 < winner:
        s = 0
    elif col_rocks + start_heap_1 >= winner and pl_position < 5:
        s = 0 
    else:
        if pl_position % 2 == 0:
            s1 = game(col_rocks + v_hod1, start_heap_1, pl_position + 1,  v_hod1, v_hod2, v_hod3, winner)
            s2 = game(col_rocks + v_hod2, start_heap_1, pl_position + 1,  v_hod1, v_hod2, v_hod3, winner)
            s3 = game(col_rocks * v_hod3, start_heap_1, pl_position + 1,  v_hod1, v_hod2, v_hod3, winner)
            s = s1 or s2 or s3
        elif pl_position % 2 != 0:
            s1 = game(col_rocks + v_hod1, start_heap_1, pl_position + 1,  v_hod1, v_hod2, v_hod3, winner)
            s2 = game(col_rocks + v_hod2, start_heap_1, pl_position + 1,  v_hod1, v_hod2, v_hod3, winner)
            s3 = game(col_rocks * v_hod3, start_heap_1, pl_position + 1,  v_hod1, v_hod2, v_hod3, winner)
            s = s1 and s2 and s3
    return s

for s in range(1, 200):
    if game(s, 0, 1, 1, 1, 5, 201) == 1:
        print(s)
        