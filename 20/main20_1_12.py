"""     Игрок за один ход может добавить 1 или 4 камня либо 
    увеличить количество камней в кучев 3 раза """
"""     1 <= Начальное значение <= 201, игра заканчивается еслив куче >= 202 камня """
""" Для игры описанной в задании 19. Найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
— Петя не может выиграть за один ход;
— Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня. """

def game(col_rocks, pl_position, v_hod1, v_hod2, v_hod3, winner): #р - позиция игрока. если четная, то значит, ход Вани, если нет - ход Пети 
    if pl_position == 4 and col_rocks >= winner:
        s = 1
    elif pl_position == 4 and col_rocks < winner:
        s = 0
    elif col_rocks >= winner and pl_position < 4:
        s = 0 
    else:
        if pl_position % 2 != 0:    # стратегия победителя 
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
for s in range(1, 202):
    if game(s, 1,1,4,3,202) == 1:
        print(s)
 
