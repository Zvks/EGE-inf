f = open("C:\\Users\\user\\ege_inf\\EGE-inf\\EGE_2024_Informatika_20var_variant-01_Faily\\9\\9 вариант 1.csv")
counter = 0
for s in f:
    s_list = list(map(int, s.split(";")))
    s_repeat = []
    pair = 0
    for i in s_list:
        if s_list.count(i) == 3 and not(i in s_repeat):
            s_repeat.append(i)
        if s_list.count(i) == 2:
            pair += 1
            break
    if len(s_repeat) == 2 and pair == 0 and not(max(s_list) in s_repeat):
        counter += 1
        print(s_list)
print(counter)