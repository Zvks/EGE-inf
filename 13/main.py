print(bin(255)[2:], bin(255)[2:], bin(255)[2:], bin(192)[2:])
print(bin(211)[2:])
print(int("11100000", 2))
print(224&211)
# counter_IP = 0
# for i in range(256):
#     n1 = bin(i&142)[2:]
#     for j in range(256):
#         n2 = bin(j&108)[2:]
#         for i2 in range(256):
#             n3 = bin(i2&56)[2:]
#             for j2 in range(256):
#                 n4 = bin(j2&118)[2:]
#                 if (n1.count("1") + n2.count("1")) > (n3.count("1") +  n4.count("1")):
#                     counter_IP += 1
#                     print(n1, n2, n3, n4)
# print(counter_IP)