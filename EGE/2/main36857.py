#  ((¬x ∨ z) ≡ (y ∧ ¬w)) → (z ∧ y)
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not((not(x) or z) == (y and not(w))) or (z and y)) == 0:
                    print(x,y,z,w)