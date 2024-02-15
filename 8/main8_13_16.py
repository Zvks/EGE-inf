count = 0
for n1 in range(1,5):
    for n2 in range(5):
        for n3 in range(5):
            if not(n1 < n2 or n2 < n3):
                count += 1
print(count)