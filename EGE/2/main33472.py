# (w → x) ∧ ((y → z) ≡ (x → y))
print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((not(w) or x) and ((not(y) or z) == (not(x) or y))) == True:
                    print(w, x, y, z)