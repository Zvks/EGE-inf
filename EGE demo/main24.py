f = open("/home/user/Documents/EGE demo/®¯_ä ©«ë/ ¤ ­¨¥ 24/24_2024.txt")
t_counter = 0
posl_counter = 0
len_posl_list = []
for s in f:
    for symbol in s:
        posl_counter += 1
        if symbol == "T":
            t_counter += 1
            if t_counter == 101:
                len_posl_list.append(posl_counter)
                posl_counter = 0
                t_counter = 0
print(max(len_posl_list))