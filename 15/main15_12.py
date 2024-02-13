B = [i for i in range(4,19)]
C = [i for i in range(12,41)]
A = []

for x in range(1,100):
    if  not(not(x in A)) <= ((x in B) == (x in C)) : # внимание, скобки!
        A.append(x)
print(max(A)- min(A))