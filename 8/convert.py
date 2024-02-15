def convert_to(number, base, razr):
#   digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    st = "А"*razr
    digits = "АЗЛОПЬ"
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
    if s.count("А") == 1 and s.count("Ь") <= 1 and s.count("З") <= 2:
        print(s, i+1)
        break