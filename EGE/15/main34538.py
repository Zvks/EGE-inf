# ( ¬(x ∈ A) → (¬(x ∈ P)) )
# ((x ∈ Q)→ (x ∈ A))
P = [i for i in range(30,46)]
Q = [i for i in range(40,56)]
A_res = []
for A in range(500):
    f = bool(((not(not(A)) or (not(A in P))) and (not(A inQ) or A)))
    if f == True:
        A_res.append(A)
print(len(A_res), A_res, f)