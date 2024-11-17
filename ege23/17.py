a = [0] * 20
a[2] = 1
for i in range(3, 20):
    a[i] += a[i-1]
    a[i] += a[i-3]
    if int(i ** 0.5) ** 2 == i:
        a[i] += a[int(i ** 0.5)]
print(a[19], a)