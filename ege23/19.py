a = [0] * 28
a[11] = 1
for i in range(12, 28):
    a[i] += a[i-1]
    a[i] += a[i-10]
print(a[27], a)