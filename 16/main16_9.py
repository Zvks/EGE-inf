import json
import sys
sys.setrecursionlimit(3000)
def read_json(path):
    with open(path, "r") as fh:
        dict_ = json.load(fh)
    return dict_

def Func(n):
    if n <= 1: 
        res = 1
    elif n > 1 and n % 2 != 0: 
        res = 5 * n + Func(n-1) + Func(2)
    elif n > 1 and n % 2 == 0: 
        res = 3 * Func(n-1)   
    return res

path = "/home/user/Documents/EGE inf/16/16/16.json"
data = read_json(path)
s1 = Func(data['n1'])
print(s1)