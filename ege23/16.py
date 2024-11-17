a = [0] * 39
a[2] = 1
for i in range(3, 39):
    a[i] += a[i-1]
    if i % 2 == 0:
        a[i] += a[i//2]
    if int(i ** 0.5) ** 2 == i:
        a[i] += a[int(i ** 0.5)]
print(a[38], a)