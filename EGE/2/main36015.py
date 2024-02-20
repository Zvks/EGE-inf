# print("x w z y")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if ((not(x) or y) or not(not(w) or z)) == False:
#                     print(x, w, z, y)
print(450 * 8 * 1024)
print(768*600)
print(450 * 8 * 1024/ 768*600)
n = 450 * 8 * 1024- 768*600
count = 0
while n >= 2:
    n = n / 2
    count += 1
print(n, count)
print((450 * 8 * 1024 - 768*600) / (768 * 600))
print(int("1111111", 2))