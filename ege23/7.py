a = [0] * 16
a[1] = 1
for i in range(2, 16):
    a[i] += a[i-3]
    a[i] += a[i-1]
    if i % 2 == 0:
        a[i] += a[i//2]
print(a[15])