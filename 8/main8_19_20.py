count = 0
for n1 in range(1,7):
    for n2 in range(1,7):
        for n3 in range(1,7):
            for n4 in range(1,7):
                for n5 in range(1,7):
                    s = str(n1) + str(n2) + str(n3) + str(n4) + str(n5)
                    if s.count("1") == 1:
                        count += 1
print(count)
print(5*5*5*5*5)
# 1 - 12345, 2,3,4,5-23456
def convert_to(number, base, razr):
#   digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    st = "1"*razr
    digits = "123456"
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    len_res = len(result)
    st = st[len_res:] + result
    return st

num = 0
for i in range(1000000):
    s = convert_to(i, 6,5)
    if s.count("1") == 1:
        num += 1
    if s == "66666":
        break
print(num)