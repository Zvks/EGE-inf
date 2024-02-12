import json
import sys
sys.setrecursionlimit(3000)
def read_json(path):
    with open(path, "r") as fh:
        dict_ = json.load(fh)
    return dict_

def Func(n):
    if n < 3: 
        res = n
    elif n > 2 and n % 2 == 0: 
        res = 2 * (n - 1) + Func(n - 1) + 2
    elif n > 2 and n % 2 != 0: 
        res = 2 * (n + 1) + Func(n - 2) - 5  
    return res

path = "/home/user/Documents/EGE inf/16/16/16.json"
data = read_json(path)
s1 = Func(data['n1'])
print(s1)
