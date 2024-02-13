B = [i for i in range(14,21)]
C = [i for i in range(15,28)]
A = []

for x in range(1,100):
    if  not(not(x in A)) <= ((x in B) == (x in C)) : # внимание, скобки!
        A.append(x)
print(max(A)- min(A))