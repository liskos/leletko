a = [0] * 28
a[5] = 1
for i in range(6, 28):
    a[i] += a[i-3]
    if i % 3 == 0:
        a[i] += a[i//3]
print(a[27])