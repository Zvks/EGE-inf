f = open("C:\\Users\\user\\ege_inf\\EGE-inf\\EGE\\9\\107_9.csv")
counter = 0
for s in f:
    st = list(map(int, s.split(";")))
    st.sort()
    if st[-1] < st[-3] + st[-4]:
        counter += 1
        print(st)
print(counter)
