import json
import sys
sys.setrecursionlimit(3000)
# def read_json(path):
#     with open(path, "r") as fh:
#         dict_ = json.load(fh)
#     return dict_

def Func(n):
    if n < 3: 
        res = 1
    elif n > 2 and n % 2 != 0: 
        res = Func(n - 1) + Func(n - 2)
    elif n > 2 and n % 2 == 0: 
        res = sum(Func(i) for i in range (1,n))   
    return res

path = "/home/user/Documents/EGE inf/16/16/16.json"
#data = read_json(path)
s1 = Func(39)
print(s1)
