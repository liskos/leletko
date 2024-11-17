a = [0] * 41
a[2] = 1
for i in range(3, 41):
    a[i] += a[i-2]
    if i % 2 == 0:
        a[i] += a[i//2]
print(a[40], a)