import json
import sys

sys.setrecursionlimit(3000)
p1 = 0
p2 = 1
global_sum = 0
def read_json(path):
    with open(path, "r") as fh:
        dict_ = json.load(fh)
    return dict_
    
def Gen():
    global p1
    global p2
    res = 2*(p1+ p2)
    p1 = p2
    p2 = res
    return res


def Func(n):
    global global_sum
    if n < 3: 
        res = 1
    elif n > 2 and n % 2 != 0: 
        res = Func(n - 1) - Func(n - 2)
        global_sum += res
    elif n > 2 and n % 2 == 0: 

        global_sum = global_sum + Gen()
        res = global_sum
    return res

path = "/home/user/Documents/EGE inf/16/16/16.json"
data = read_json(path)
s1 = Func(data['n1'])
print(s1)
#41518080
# for i in range(1, 10):
#     print(Gen())