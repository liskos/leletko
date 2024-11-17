a = [0] * 28
a[2] = 1
for i in range(3, 28):
    a[i] += a[i-1]
    if i % 2 == 0:
        a[i] += a[i//2]
    if int(i ** 0.5) ** 2 == i:
        a[i] += a[int(i ** 0.5)]
print(a[27], a)