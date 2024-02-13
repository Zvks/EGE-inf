B = [i for i in range(30,42)]
C = [i for i in range(50,57)]
A = []

for x in range(100):
    if not (((x in B) or (x in C)) <= (x in A)):
        A.append(x)
print(max(A) - min(A))