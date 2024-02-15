# def convert_to(number, base, razr):
# #   digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     st = "1"+"0"*(razr - 1)
#     digits = "0123456789"
#     if base > len(digits): return None
#     result = ''
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     len_res = len(result)
#     st = st[len_res:] + result
#     return st

num = 0
for i in range(1000, 9999):
    s = str(i)
    n1 = s[0]
    n2 = s[1]
    n3 = s[2]
    n4 = s[3]
    if  (n1 == n2 and n1 != n3 and n1 != n4 and n3 != n4) \
        or (n2 == n3 and n2 != n4 and n3 != n1 and n1 != n4) \
        or (n3 == n4 and n3 != n2 and n1 != n3 and n1 != n2):
            num += 1
print(num)