a = [0] * 71
a[2] = 1
for i in range(3, 9):
    a[i] = a[i-1]
    if i % 3 == 0:
        a[i] += a[i//3]
    if i % 4 == 0:
        a[i] += a[i//4]

b = [0] * 71
b[8] = a[8]
for i in range(9, 71):
    b[i] = b[i - 1]
    if i % 3 == 0:
        b[i] += b[i // 3]
    if i % 4 == 0:
        b[i] += b[i // 4]
    if i == 35:
        b[i] = 0
print(b[70])