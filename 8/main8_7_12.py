# class BreakLoops(Exception):
#     pass
 
# try:
#     num = 0
#     for n1 in "КНОРСЯ":
#         for n2 in "КНОРСЯ":
#             for n3 in "КНОРСЯ":
#                 for n4 in "КНОРСЯ":
#                     for n5 in "КНОРСЯ":
#                         for n6 in "КНОРСЯ":
#                             num += 1
#                             col_k = 0
#                             col_y = 0
#                             s = n1 + n2 + n3 + n4 + n5 + n6
#                             for i in s:
#                                 if i == "К":
#                                     col_k += 1
#                                 if i == "Я":
#                                     col_y += 1
#                             if (col_k <= 3 and col_y == 2):
#                                 print(num, n1, n2, n3, n4, n5, n6)
#                                 raise BreakLoops
# except BreakLoops:
#     pass 

def convert_to(number, base, razr):
#   digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    st = "К"*razr
    digits = "КНОРСЯ"
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    len_res = len(result)
    st = st[len_res:] + result
    return st

for i in range(1000000):
    s = convert_to(i, 6,6)
    if s.count("Я") == 2 and s.count("К") <= 3:
        print(s, i+1)
        break