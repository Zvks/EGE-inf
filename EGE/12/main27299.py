for i in range(61, 121):
    s = "1"*i
    while ('111' in s):
        if ('111' in s): 
            s=s.replace ('111','2',1)
        if ("222" in s):
            s=s.replace ('222','11',1)
    if s == "221":        
        print(s, i)
        break
print(s, i)
s = "1" * 61
while ('111' in s):
    if ('111' in s): 
        s=s.replace ('111','2',1)
    if ("222" in s):
        s=s.replace ('222','11',1)
print(s)