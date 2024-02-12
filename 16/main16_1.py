import json
import sys
sys.setrecursionlimit(3000)
def read_json(path):
    with open(path, "r") as fh:
        dict_ = json.load(fh)
    return dict_

def Func(n):
    if n == 1:
        res = 5
    elif n > 1:
        res = Func(n - 1) + 2*n + 1
    return res

path = "/home/user/Documents/EGE inf/16/16/16.json"
data = read_json(path)
s1 = Func(data['n1'])
s2 = Func(data['n2'])
print(s1 - s2)
