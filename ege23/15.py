a = [0] * 16
a[3] = 1
for i in range(3, 16):
    a[i] += a[i-1]
    a[i] += a[i-3]
    if i % 2 == 0:
        a[i] += a[i//2]
print(a[15], a)